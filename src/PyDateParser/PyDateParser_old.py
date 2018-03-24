import re
import operator
from datetime import datetime, timedelta, tzinfo

"""
    Parses string and returns datetime in UTC by default
"""


class PyDateParser:
    def __init__(self):

        # this will hold the relative datetime value
        self.__relative_datetime = None

        self.__date_string = ""

        # shortest string will be like "1d", which is 2 chars
        self.__min_length = 2

        # min and max number of tokens
        self.__min_tokens = 1
        self.__max_tokens = 3

        self.__regexp_number = "(\d+)"
        self.__regexp_timeframe = "([s|m|h|d|w])"
        self.__regexp_operators = "([+-])?"
        self.__operand_keywords = ["now", "yday", "tmrw", "dby", "dat"]

        self.__regexp_syntax = self.__regexp_operators + self.__regexp_number + \
                               self.__regexp_timeframe

        self.__sample_pattern = "Syntax: enums | enums[+|-] Int [s|m|h|w] \r" \
                                "s = seconds, m = minute, h = hour, w = week \r" \
                                "\r Supported enums \r" \
                                "-----------------------\r" \
                                "now = current date time, \r" \
                                "yday = yesterday, \r" \
                                "tmrw = tomorrow, \r" \
                                "dby = day before yesterday, \r" \
                                "dat = day after yesterday \r\r" \
                                "Example: now, yday, tmrw, now-1d, now+1d, 1d, yday-1d"

    """
    Supported values
    [+|-][0-9][s|m|d|w] = 1h  //1 hour from now
                              -1h //1 hour before

    now = current date time

    now-1d = current date time minus 1 day

    now+1d = current date time plus 1 day

    """

    def parse(self, date_string, relative_datetime=None):

        if relative_datetime is None:
            self.__relative_datetime = datetime.utcnow()

        date_string = self.cleanup_string(date_string)

        if self.__is_valid(date_string):
            tokens = self.__parse_tokens(date_string)
            return self.__process_tokens(tokens)
        else:
            raise ValueError("Invalid date_string")

    def cleanup_string(self, date_string):
        # remove spaces
        return date_string.replace(" ", "")

    """
    basic validation of input parameters
    """

    def __is_valid(self, date_string):
        if not date_string:
            raise ValueError("Empty value detected.")

        elif len(date_string) < self.__min_length:
            raise ValueError("Invalid string length; should have atleast {} characters.".format(self.__minlength))

        elif not re.match(self.__regexp_syntax, date_string) and \
                        date_string not in self.__operand_keywords:
            raise ValueError("Invalid syntax.")

        return True

    def __parse_operand(self, dict_operand):

        result = {}

        if dict_operand:
            # if simple operand like now, tmrw, etc
            if dict_operand in self.__operand_keywords:
                result["type"] = "simple"
                result["value"] = dict_operand

            # complex operand, like 1s, 2d, 4s etc
            else:
                timeframe_val = self.__retrieve_timeframe(dict_operand)
                number_val = self.__retrieve_number(dict_operand)

                result["type"] = "complex"
                result["value"] = {"number": number_val,
                                   "timeframe": timeframe_val}
        else:
            raise ValueError("No operand to parse")

        return result

    def __retrieve_timeframe(self, value):

        result = re.search(self.__regexp_timeframe, value)
        if result:
            return value[result.start():result.end()]
        else:
            return None

    def __retrieve_number(self, value):

        result = re.search(self.__regexp_number, value)
        if result:
            return value[result.start():result.end()]
        else:
            return None

    def __validate_operand(self, value):

        complex_operand_regexp = self.__regexp_number + self.__regexp_timeframe
        if re.search(complex_operand_regexp, value):
            return True
        elif value in self.__operand_keywords:
            return True
        else:
            raise ValueError("Invalid format detected '{}'".format(value))

    def __parse_tokens(self, date_string):
        tokens = {}

        # this matches string like -12s, 4h, 1w etc
        if re.search(self.__regexp_syntax, date_string):

            # see if the + or - operator is present
            result = re.search(self.__regexp_operators, date_string)

            # if string contains -12h or +12h get the operator
            if result and (result.start() != 0 and result.end() != 0):
                # get the operator defined in the string
                operator_start_pos = result.start()
                operator_end_pos = result.end()

                tokens["operator"] = date_string[operator_start_pos:operator_end_pos]

                # read from where the operator char ends to all the way to end of string
                operand2 = date_string[operator_end_pos:]
            else:
                # if not operator specified default to +
                tokens["operator"] = "+"

                # as the input value doesn't contain operator consider entire input as second operand
                operand2 = date_string

            # set first operand always defaults to "now" as values passed like -12h, 1h, 3w
            # will always be added or subtracted against current datetime
            operand1 = "now"

            if self.__validate_operand(operand1):
                # get the first operand, 0 to position where the operator starts
                tokens["operand1"] = self.__parse_operand(operand1)

            if self.__validate_operand(operand2):
                # get the second operand, position where the operator end till end of string
                tokens["operand2"] = self.__parse_operand(operand2)

        # check for string like now, yday, tmrw etc
        elif date_string in self.__operand_keywords:

            if self.__validate_operand(date_string):
                tokens["operand1"] = self.__parse_operand(date_string)

        # throw invalid token exception
        else:
            raise ValueError("Invalid format. Supported formats: {}".format(self.__sample_pattern))

        return tokens

    # receives value of
    # {'operator': '-', 'operand1': {'type': 'simple', 'value': 'now'}, 'operand2': {'type': 'complex', 'value': {'number': '1', 'timeframe': 'd'}}}
    def __process_tokens(self, tokens):

        ops = {"+": operator.add,
               "-": operator.sub}

        # means the token contain two operands and one operator
        if "operator" in tokens:
            operator_val = tokens["operator"]

            operand1 = self.__process_operand(tokens["operand1"])
            operand2 = self.__process_operand(tokens["operand2"])

            return ops[operator_val](operand1, operand2)

        # means the token contain only single operand
        elif "operand1" in tokens:
            return self.__process_operand(tokens["operand1"])

        else:
            raise ValueError("Invalid Tokens")

    def __process_operand(self, operand):

        now = self.__relative_datetime

        if "type" in operand and operand["type"] == "simple":

            simple_vals = {
                "now": now,
                "tmrw": now + timedelta(days=1),  # tomorrow
                "dat": now + timedelta(days=2),  # day after tomorrow
                "yday": now - timedelta(days=1),  # yesterday
                "dby": now - timedelta(days=2)  # day before yesterday
            }

            return simple_vals[operand["value"]]

        elif "type" in operand and operand["type"] == "complex":

            val = int(operand["value"]["number"])

            complex_vals = {
                "s": timedelta(seconds=val),
                "m": timedelta(minutes=val),
                "h": timedelta(hours=val),
                "d": timedelta(days=val),
                "w": timedelta(weeks=val)
            }

            return complex_vals[operand["value"]["timeframe"]]

        else:
            raise ValueError("Invalid operand")
