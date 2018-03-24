import sys
import unittest
from datetime import datetime, timedelta, tzinfo
from dateutil import parser

sys.path.append("../src/PyDateParser")
from PyDateParser import PyDateParser


class PyDateParseTest(unittest.TestCase):
    def setUp(self):
        self.__obj = PyDateParser()

    def tearDown(self):
        self.__obj = None

    def test_utc_now(self):
        val = self.__obj.parse("now")
        now = datetime.utcnow()

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        self.assertEqual(str(parsed_datetime), str(actual_datetime))


    def test_utc_add_second(self):
        val = self.__obj.parse("1s")
        now = datetime.utcnow() + timedelta(seconds=1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        self.assertEqual(str(parsed_datetime), str(actual_datetime))


    def test_utc_add_minute(self):
        val = self.__obj.parse("1m")
        now = datetime.utcnow() + timedelta(minutes=1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        self.assertEqual(str(parsed_datetime), str(actual_datetime))


    def test_utc_add_hour(self):
        val = self.__obj.parse("1h")
        now = datetime.utcnow() + timedelta(hours=1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        self.assertEqual(str(parsed_datetime), str(actual_datetime))


# test
if __name__ == '__main__':
    unittest.main()
