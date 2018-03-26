import sys
import unittest
import random
from datetime import datetime, timedelta, tzinfo
from dateutil import parser

sys.path.append("../src/PyDateParser")
from PyDateParser import PyDateParser


class PyDateParseKeywordTest(unittest.TestCase):
    def setUp(self):
        self.__obj = PyDateParser()

    def tearDown(self):
        self.__obj = None

    def test_keyword_utc_now(self):
        val = self.__obj.parse("now")
        now = datetime.utcnow()

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_now parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime, actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_keyword_present_date_time_now(self):
        now = datetime.now()
        val = self.__obj.parse("now", relative_datetime=now)


        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_keyword_present_date_time_now parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                       actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)


    def test_keyword_tmrw(self):
        val = self.__obj.parse("tmrw")
        now = datetime.utcnow() + timedelta(days=1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_keyword_tmrw parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime, actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_keyword_yday(self):
        val = self.__obj.parse("yday")
        now = datetime.utcnow() + timedelta(days=-1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_keyword_yday parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime, actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    # dby day bef yday
    def test_keyword_dby(self):
        val = self.__obj.parse("dby")
        now = datetime.utcnow() + timedelta(days=-2)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_keyword_dby parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime, actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    # dat day aftr tmrw
    def test_keyword_dat(self):
        val = self.__obj.parse("dat")
        now = datetime.utcnow() + timedelta(days=2)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_keyword_dat parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime, actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)


# **********************************************************************************************************************
class PyDateParseAddTimeTest(unittest.TestCase):
    def setUp(self):
        self.__obj = PyDateParser()

    def tearDown(self):
        self.__obj = None

    def test_utc_add_second(self):
        val = self.__obj.parse("1s")
        now = datetime.utcnow() + timedelta(seconds=1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_second parsed_datetime:{} actual_datetime: {} ".format(
            parsed_datetime, actual_datetime)

        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_current_date_time_add_second(self):
        now = datetime.now() + timedelta(seconds=1)
        val = self.__obj.parse("1s", relative_datetime=datetime.now())


        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_current_date_time_add_second parsed_datetime:{} actual_datetime: {} ".format(
            parsed_datetime, actual_datetime)

        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_minute(self):
        val = self.__obj.parse("1m")
        now = datetime.utcnow() + timedelta(minutes=1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_minute parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                        actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_hour(self):
        val = self.__obj.parse("1h")
        now = datetime.utcnow() + timedelta(hours=1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_hour parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                      actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_week(self):
        val = self.__obj.parse("1w")
        now = datetime.utcnow() + timedelta(weeks=1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_week parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                      actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_random_seconds(self):
        rnd_secs = random.randint(2, 3600)
        val = self.__obj.parse("{}s".format(rnd_secs))
        now = datetime.utcnow() + timedelta(seconds=rnd_secs)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_random_seconds parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_random_minutes(self):
        rnd_mins = random.randint(2, 1000)
        val = self.__obj.parse("{}m".format(rnd_mins))
        now = datetime.utcnow() + timedelta(minutes=rnd_mins)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_random_minutes parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_random_hours(self):
        rnd_hour = random.randint(2, 1000)
        val = self.__obj.parse("{}h".format(rnd_hour))
        now = datetime.utcnow() + timedelta(hours=rnd_hour)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_random_hours parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                              actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_random_days(self):
        rnd_days = random.randint(2, 100)
        val = self.__obj.parse("{}d".format(rnd_days))
        now = datetime.utcnow() + timedelta(days=rnd_days)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_random_days parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                             actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_random_weeks(self):
        rnd_week = random.randint(2, 100)
        val = self.__obj.parse("{}w".format(rnd_week))
        now = datetime.utcnow() + timedelta(weeks=rnd_week)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_random_weeks parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                              actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)


# **********************************************************************************************************************
class PyDateParseSubtractTimeTest(unittest.TestCase):
    def setUp(self):
        self.__obj = PyDateParser()

    def tearDown(self):
        self.__obj = None

    def test_present_dateime_time_subtract_second(self):
        val = self.__obj.parse("-1s", relative_datetime=datetime.now())
        now = datetime.now() + timedelta(seconds=-1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_present_dateime_time_subtract_second parsed_datetime:{} actual_datetime: {} ".format(
            parsed_datetime, actual_datetime)

        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_second(self):
        val = self.__obj.parse("-1s")
        now = datetime.utcnow() + timedelta(seconds=-1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_second parsed_datetime:{} actual_datetime: {} ".format(
            parsed_datetime, actual_datetime)

        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_minute(self):
        val = self.__obj.parse("-1m")
        now = datetime.utcnow() + timedelta(minutes=-1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_minute parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                             actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_hour(self):
        val = self.__obj.parse("-1h")
        now = datetime.utcnow() + timedelta(hours=-1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_hour parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                           actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_week(self):
        val = self.__obj.parse("-1w")
        now = datetime.utcnow() + timedelta(weeks=-1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_week parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                           actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_random_seconds(self):
        rnd_secs = random.randint(2, 3600)
        val = self.__obj.parse("-{}s".format(rnd_secs))
        now = datetime.utcnow() + timedelta(seconds=rnd_secs * -1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_random_seconds parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                     actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_random_minutes(self):
        rnd_mins = random.randint(2, 1000)
        val = self.__obj.parse("-{}m".format(rnd_mins))
        now = datetime.utcnow() + timedelta(minutes=rnd_mins * -1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_random_minutes parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                     actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_random_hours(self):
        rnd_hour = random.randint(2, 1000)
        val = self.__obj.parse("-{}h".format(rnd_hour))
        now = datetime.utcnow() + timedelta(hours=rnd_hour * -1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_random_minutes parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                     actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_random_days(self):
        rnd_days = random.randint(2, 100)
        val = self.__obj.parse("-{}d".format(rnd_days))
        now = datetime.utcnow() + timedelta(days=rnd_days * -1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_random_days parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                  actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_random_weeks(self):
        rnd_week = random.randint(2, 100)
        val = self.__obj.parse("-{}w".format(rnd_week))
        now = datetime.utcnow() + timedelta(weeks=rnd_week * -1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_random_weeks parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                   actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)


# **********************************************************************************************************************
class PyDateParseAddFloatTimeTest(unittest.TestCase):
    def setUp(self):
        self.__obj = PyDateParser()

    def tearDown(self):
        self.__obj = None

    def test_utc_add_second(self):
        val = self.__obj.parse("1.5s")
        now = datetime.utcnow() + timedelta(seconds=1.5)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_second parsed_datetime:{} actual_datetime: {} ".format(
            parsed_datetime, actual_datetime)

        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_minute(self):
        val = self.__obj.parse("1.5m")
        now = datetime.utcnow() + timedelta(minutes=1.5)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_minute parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                        actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_hour(self):
        val = self.__obj.parse("1.5h")
        now = datetime.utcnow() + timedelta(hours=1.5)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_hour parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                      actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_week(self):
        val = self.__obj.parse("1.5w")
        now = datetime.utcnow() + timedelta(weeks=1.5)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_week parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                      actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_random_seconds(self):
        rnd_secs = random.randint(2, 3600) + random.uniform(.1, .9)
        val = self.__obj.parse("{}s".format(rnd_secs))
        now = datetime.utcnow() + timedelta(seconds=rnd_secs)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_random_seconds parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_random_minutes(self):
        rnd_mins = random.randint(2, 1000) + random.uniform(.1, .9)
        val = self.__obj.parse("{}m".format(rnd_mins))
        now = datetime.utcnow() + timedelta(minutes=rnd_mins)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_random_minutes parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_random_hours(self):
        rnd_hour = random.randint(2, 1000) + random.uniform(.1, .9)
        val = self.__obj.parse("{}h".format(rnd_hour))
        now = datetime.utcnow() + timedelta(hours=rnd_hour)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_random_hours parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                              actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_random_days(self):
        rnd_days = random.randint(2, 100) + random.uniform(.1, .9)
        val = self.__obj.parse("{}d".format(rnd_days))
        now = datetime.utcnow() + timedelta(days=rnd_days)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_random_days parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                             actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_add_random_weeks(self):
        rnd_week = random.randint(2, 100) + random.uniform(.1, .9)
        val = self.__obj.parse("{}w".format(rnd_week))
        now = datetime.utcnow() + timedelta(weeks=rnd_week)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_add_random_weeks parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                              actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)


# **********************************************************************************************************************
class PyDateParseSubtractFloatTimeTest(unittest.TestCase):
    def setUp(self):
        self.__obj = PyDateParser()

    def tearDown(self):
        self.__obj = None

    def test_utc_subtract_second(self):
        val = self.__obj.parse("-1.5s")
        now = datetime.utcnow() + timedelta(seconds=-1.5)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_second parsed_datetime:{} actual_datetime: {} ".format(
            parsed_datetime, actual_datetime)

        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_minute(self):
        val = self.__obj.parse("-1.5m")
        now = datetime.utcnow() + timedelta(minutes=-1.5)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_minute parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                             actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_hour(self):
        val = self.__obj.parse("-1.5h")
        now = datetime.utcnow() + timedelta(hours=-1.5)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_hour parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                           actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_week(self):
        val = self.__obj.parse("-1.5w")
        now = datetime.utcnow() + timedelta(weeks=-1.5)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_week parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                           actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_random_seconds(self):
        rnd_secs = random.randint(2, 3600) + random.uniform(.1, .9)
        val = self.__obj.parse("-{}s".format(rnd_secs))
        now = datetime.utcnow() + timedelta(seconds=rnd_secs * -1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_random_seconds parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                     actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_random_minutes(self):
        rnd_mins = random.randint(2, 1000) + random.uniform(.1, .9)
        val = self.__obj.parse("-{}m".format(rnd_mins))
        now = datetime.utcnow() + timedelta(minutes=rnd_mins * -1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_random_minutes parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                     actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_random_hours(self):
        rnd_hour = random.randint(2, 1000) + random.uniform(.1, .9)
        val = self.__obj.parse("-{}h".format(rnd_hour))
        now = datetime.utcnow() + timedelta(hours=rnd_hour * -1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_random_minutes parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                     actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_random_days(self):
        rnd_days = random.randint(2, 100) + random.uniform(.1, .9)
        val = self.__obj.parse("-{}d".format(rnd_days))
        now = datetime.utcnow() + timedelta(days=rnd_days * -1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_random_days parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                  actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)

    def test_utc_subtract_random_weeks(self):
        rnd_week = random.randint(2, 100) + random.uniform(.1, .9)
        val = self.__obj.parse("-{}w".format(rnd_week))
        now = datetime.utcnow() + timedelta(weeks=rnd_week * -1)

        parsed_datetime = datetime(year=val.year, month=val.month, day=val.day, \
                                   hour=val.hour, minute=val.minute, second=val.second, microsecond=0)

        actual_datetime = datetime(year=now.year, month=now.month, day=now.day, \
                                   hour=now.hour, minute=now.minute, second=now.second, microsecond=0)

        fail_msg = "test_utc_subtract_random_weeks parsed_datetime:{} actual_datetime: {} ".format(parsed_datetime,
                                                                                                   actual_datetime)
        return self.assertEqual(str(parsed_datetime), str(actual_datetime), fail_msg)


# **********************************************************************************************************************
class PyDateParseNegativeTest(unittest.TestCase):
    def setUp(self):
        self.__obj = PyDateParser()

    def tearDown(self):
        self.__obj = None

    def test_invalid_keyword(self):
        with self.assertRaises(ValueError):
            val = self.__obj.parse("hey mate")

        with self.assertRaises(ValueError):
            val = self.__obj.parse(".")

    def test_invalid_syntax(self):
        with self.assertRaises(ValueError):
            val = self.__obj.parse("+")

        with self.assertRaises(ValueError):
            val = self.__obj.parse("-")

        with self.assertRaises(ValueError):
            val = self.__obj.parse("3+ew+2")

    def test_overflow_errors(self):
        with self.assertRaises(OverflowError):
            val = self.__obj.parse("99999999999s")

        with self.assertRaises(OverflowError):
            val = self.__obj.parse("99999999999m")

        with self.assertRaises(OverflowError):
            val = self.__obj.parse("99999999999h")

        with self.assertRaises(OverflowError):
            val = self.__obj.parse("99999999999w")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            val = self.__obj.parse("")

    def test_Null(self):
        with self.assertRaises(ValueError):
            val = self.__obj.parse(None)


# **********************************************************************************************************************
if __name__ == '__main__':
    unittest.main()
