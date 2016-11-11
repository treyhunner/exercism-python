from datetime import timedelta


def add_gigasecond(original_date):
    return original_date + timedelta(seconds=10**9)
