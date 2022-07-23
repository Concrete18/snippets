import unittest
import datetime as dt

# classes
from snippets.datetime_funcs import datetime_funcs


class TestStringMethods(unittest.TestCase):
    def test_get_year(self):
        test = datetime_funcs()
        date_tests = {
            "this is not a date": "Invalid Date",
            "Sep 14, 2016": "2016",
            "25 Apr, 1991": "1991",
            "16 Nov, 2009": "2009",
            "Mai 25, 1991": "1991",
            "Apr , 2015": "2015",
        }
        for date, bool in date_tests.items():
            result = test.get_year(date)
            self.assertEqual(result, bool)

    def test_hours_played(self):
        test = datetime_funcs()
        time_hours_played = {
            800: 13.3,
            30: 0.5,
            2940: 49,
            0: None,
        }
        for minutes_played, answer in time_hours_played.items():
            result = test.hours_played(minutes_played)
            self.assertEqual(result, answer)

    def test_time_passed(self):
        test = datetime_funcs()
        # tests function when given minutes
        minutes_tests = {
            12: "12.0 Minute(s)",
            59: "59.0 Minute(s)",
            60: "1.0 Hour(s)",
            800: "13.3 Hour(s)",
            1439: "1.0 Day(s)",
            1440: "1.0 Day(s)",
            1441: "1.0 Day(s)",
            2940: "2.0 Day(s)",
            1440 * 7: "1.0 Week(s)",
            525600: "1.0 Year(s)",
        }
        for minutes, answer in minutes_tests.items():
            result = test.convert_time_passed(min=minutes)
            self.assertEqual(result, answer)

        # tests function when given hours
        hours_tests = {
            0.2: "12.0 Minute(s)",
            1: "1.0 Hour(s)",
            13.3: "13.3 Hour(s)",
            24: "1.0 Day(s)",
            48: "2.0 Day(s)",
        }
        for hours, answer in hours_tests.items():
            result = test.convert_time_passed(hr=hours)
            self.assertEqual(result, answer)

        # tests function when given days
        days_tests = {
            1: "1.0 Day(s)",
            5.8: "5.8 Day(s)",
            21: "3.0 Week(s)",
            365: "1.0 Year(s)",
        }
        for days, answer in days_tests.items():
            result = test.convert_time_passed(day=days)
            self.assertEqual(result, answer)

        # tests function when given weeks
        weeks_tests = {
            4.4: "1.0 Month(s)",
            # 3.5: "24.5 Day(s)",
            # 52.971: "1.0 Year(s)",
        }
        for weeks, answer in weeks_tests.items():
            result = test.convert_time_passed(wk=weeks)
            self.assertEqual(result, answer)

        # # tests function when given months TODO
        # days_tests = {
        #     1: "1.0 Month(s)",
        #     18: "1.5 Year(s)",
        #     21: "3.0 Week(s)",
        #     365: "1.0 Year(s)",
        # }
        # for days, answer in days_tests.items():
        #     result = test.convert_time_passed(day=days)
        #     self.assertEqual(result, answer)

        # # tests function when given years TODO
        # days_tests = {
        #     1: "1.0 Day(s)",
        #     5.8: "5.8 Day(s)",
        #     21: "3.0 Week(s)",
        #     365: "1.0 Year(s)",
        # }

        for days, answer in days_tests.items():
            result = test.convert_time_passed(day=days)
            self.assertEqual(result, answer)
        # tests all args at once
        result = test.convert_time_passed(min=60, hr=23, day=30, mnth=11, yr=1)
        self.assertEqual(result, "2.0 Year(s)")

    def test_days_since(self):
        test = datetime_funcs()
        date_tests = {
            2: dt.datetime(2022, 4, 22),
            10: dt.datetime(2022, 4, 14),
            365: dt.datetime(2021, 4, 24),
        }
        past_date = dt.datetime(2022, 4, 24)
        for answer, current_date in date_tests.items():
            result = test.days_since(current_date, past_date)
            self.assertEqual(result, answer)


if __name__ == "__main__":
    unittest.main()
