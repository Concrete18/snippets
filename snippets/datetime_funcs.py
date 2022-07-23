import datetime as dt
import re


class datetime_funcs:
    def hours_played(minutes):
        """
        Converts `minutes` to a hours in decimal form.
        """
        hours_played = round(minutes / 60, 1)
        if hours_played == 0.0:
            return None
        return round(minutes / 60, 1)

    @staticmethod
    def string_to_date(date: str):
        """
        Converts String `date` in MM/DD/YYYY format to datetime object.
        """
        return dt.datetime.strptime(date, "%m/%d/%Y")

    def get_year(date_string):
        """
        Gets the year from `date_string`.
        """
        year = re.search(r"[0-9]{4}", date_string)
        if year:
            return year.group(0)
        else:
            return "Invalid Date"

    @staticmethod
    def days_since(past_date, current_date=None):
        """
        Gets the days since a `past_date`.

        if `current_date` is not given then it is set to the current date.
        """
        if not current_date:
            current_date = dt.datetime.now()
        delta = current_date - past_date
        return delta.days

    def convert_time_passed(min=0, hr=0, wk=0, day=0, mnth=0, yr=0):
        """
        Outputs a string for when the time passed.
        Takes minutes:`min`, hours:`hr`, days:`day`, weeks:`wk`
        months:`mnth` and years:`yr`.

        Return format examples:

        1.0 Minute(s)

        2.3 Hour(s)

        4.5 Day(s)

        6.7 Week(s)

        8.9 Month(s)

        2.1 Years(s)
        """
        # converts all into minutes
        hours_in_day = 24
        hours_in_week = 168
        hours_in_month = 730.001
        hours_in_year = 8760
        hours = (
            hr
            + (min / 60)
            + (day * hours_in_day)
            + (wk * hours_in_week)
            + (mnth * hours_in_month)
            + (yr * hours_in_year)
        )
        rounded_hours = round(hours)
        if rounded_hours >= hours_in_year:
            time_passed = f"{round(hours/hours_in_year, 1)} Year(s)"
        elif rounded_hours >= hours_in_month:
            time_passed = f"{round(hours/hours_in_month, 1)} Month(s)"
        elif rounded_hours >= hours_in_week:
            time_passed = f"{round(hours/hours_in_week, 1)} Week(s)"
        elif rounded_hours >= hours_in_day:
            time_passed = f"{round(hours/hours_in_day, 1)} Day(s)"
        elif hours >= 1:
            time_passed = f"{round(hours, 1)} Hour(s)"
        else:
            time_passed = f"{round(hours * 60, 1)} Minute(s)"
        return time_passed
