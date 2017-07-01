from datetime import datetime, timedelta


GIGASECOND = timedelta(seconds=10**9)


def add_gigasecond(original_date: datetime) -> datetime:
    return original_date + GIGASECOND
