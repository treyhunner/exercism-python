from datetime import timedelta


GIGASECOND = timedelta(seconds=10**9)


def add_gigasecond(original_date):
    return original_date + GIGASECOND
