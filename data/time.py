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


def get_date(use_tomorrow=False, month=None, day=None):
    today = date.today()

    if use_tomorrow:
        return today + timedelta(days=1)

    if day is not None:
        # if day is not a digit it is a weekday abbreviation
        if not day.isdigit():
            return get_next_weekday_date(day)

        if month is not None and not month.isdigit():
            month = identify_month_integer_from_abbreviation(month)
        elif month is not None and month.isdigit():
            month = int(month)
        else:
            month = today.month

        return get_next_date(day=int(day), month=month)

    return today


def get_next_date(day, month):
    today = date.today()

    current_year = today.year

    try:
        current_year_date = date(year=current_year, month=month, day=day)
    except ValueError:
        raise InvalidDateException("Day: {day} and Month: {month} combination are invalid".format(day=day, month=month))

    if current_year_date < today:
        return date(year=current_year + 1, month=month, day=day)

    return current_year_date


def identify_month_integer_from_abbreviation(month_abbreviation):
    month_value = month_abbreviation_to_month_integer.get(month_abbreviation.lower())

    if month_value is None:
        raise ValueError("Unknown month: {month}".format(month=month_abbreviation))

    return month_value


def get_next_weekday_date(weekday_abbreviation):
    weekday_integer = weekday_abbreviation_to_weekday_integer.get(weekday_abbreviation.lower())

    if weekday_integer is None:
        raise ValueError("Unknown weekday: {weekday}".format(weekday=weekday_abbreviation))

    return date.today() + relativedelta(weekday=weekday_integer)
