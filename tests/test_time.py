from unittest import TestCase

from datetime import date, timedelta

from dateutil.relativedelta import relativedelta

from mock import patch
from data.time import get_next_weekday_date, identify_month_integer_from_abbreviation, get_next_date, get_date
from data.exceptions import InvalidDateException


class TestGetNextWeekdayDate(TestCase):
    def test_raise_error_for_invalid_weekday(self):
        self.assertRaises(ValueError, get_next_weekday_date, "jaebaebae")

    def test_returns_expected_next_weekday(self):
        weekday = "wed"
        expected = date.today() + relativedelta(weekday=2)
        self.assertEqual(expected, get_next_weekday_date(weekday))


class TestIdentifyMonthIntegerFromAbbreviation(TestCase):
    def test_raise_error_for_invalid_month_abbreviation(self):
        self.assertRaises(ValueError, identify_month_integer_from_abbreviation, "jaebaebae")

    def test_returns_expected_month_abbreviation(self):
        self.assertEqual(identify_month_integer_from_abbreviation("sep"), 9)


class TestGetNextDate(TestCase):
    def test_raises_for_invalid_date(self):
        self.assertRaises(InvalidDateException, get_next_date, day=1, month=13)

    def test_month_defined(self):
        today = date.today()
        self.assertEqual(today, get_next_date(day=today.day, month=today.month))

    def test_return_next_year_date(self):
        yesterday = date.today() + timedelta(days=-1)
        expected = date(year=yesterday.year + 1, month=yesterday.month, day=yesterday.day)
        self.assertEqual(expected, get_next_date(day=yesterday.day, month=yesterday.month))


class TestGetDate(TestCase):
    def test_default_returns_today(self):
        self.assertEqual(date.today(), get_date())

    def test_use_tomorrow_returns_tomorrow(self):
        tomorrow = date.today() + timedelta(days=1)
        self.assertEqual(tomorrow, get_date(use_tomorrow=True))

    @patch("data.time.get_next_weekday_date")
    def test_weekday_is_not_none(self, mocked_next_weekday):
        weekday = "weekday"
        next_weekday = "next weekday"
        mocked_next_weekday.return_value = next_weekday
        self.assertEqual(next_weekday, get_date(day=weekday))
        mocked_next_weekday.assert_called_once_with(weekday)

    @patch("data.time.identify_month_integer_from_abbreviation")
    @patch("data.time.get_next_date")
    def test_day_is_not_none_and_use_month_abbreviation(self, mocked_next_date, mocked_month_integer):
        day = "10"
        month_abbreviation = "month abbreviation"
        next_date = "next date"
        month_integer = "month integer"
        mocked_next_date.return_value = next_date
        mocked_month_integer.return_value = month_integer
        self.assertEqual(next_date, get_date(day=day, month=month_abbreviation))
        mocked_month_integer.assert_called_once_with(month_abbreviation)
        mocked_next_date.assert_called_once_with(day=10, month=month_integer)
