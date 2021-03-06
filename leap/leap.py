import datetime


def is_leap_year(year: int) -> bool:
    try:
        datetime.date(year, 2, 29)
    except ValueError:
        return False
    else:
        return True
