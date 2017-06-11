import calendar
from datetime import date, timedelta

from dateutil.relativedelta import relativedelta
from data.exceptions import InvalidDateException

month_abbreviation_to_month_integer = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12
}

weekday_abbreviation_to_weekday_integer = {
    "mon": calendar.MONDAY,
    "tue": calendar.TUESDAY,
    "wed": calendar.WEDNESDAY,
    "thu": calendar.THURSDAY,
    "fri": calendar.FRIDAY,
    "sat": calendar.SATURDAY,
    "sun": calendar.SUNDAY
}


def get_date(use_tomorrow, weekday, month, day):
    today = date.today()

    if use_tomorrow:
        return today + timedelta(days=1)

    if weekday:
        return get_date_for_next_weekday(weekday)

    if type(month) == str:
        month = month_integer(month)

    if day is not None:
        return get_next_date(day=day, month=month)

    return today


def get_next_date(day, month=None):
    today = date.today()

    if month is None:
        month = today.month

    current_year = today.year

    try:
        current_year_date = date(year=current_year, month=month, day=day)
    except ValueError:
        raise InvalidDateException("Day: {day} and Month: {month} combination are invalid".format(day=day, month=month))

    if current_year_date < today:
        return date(year=current_year + 1, month=month, day=day)

    return current_year_date


def month_integer(month):
    month_value = month_abbreviation_to_month_integer.get(month.lower())

    if month_value is None:
        raise ValueError("Unknown month: {month}".format(month=month))

    return month_value


def get_date_for_next_weekday(weekday):
    weekday_integer = weekday_abbreviation_to_weekday_integer.get(weekday.lower())

    if weekday_integer is None:
        raise ValueError("Unknown weekday: {weekday}".format(weekday=weekday))

    return date.today() + relativedelta(weekday=weekday_integer)
