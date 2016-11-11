#!/usr/bin/env python
from datetime import date, datetime, time, timedelta


class Clock(object):
    def __init__(self, h, m):
        self.dt = datetime.combine(date.today(), time(0, 0)) + \
                                   timedelta(hours=h, minutes=m)

    def add(self, m):
        self.dt += timedelta(minutes=m)
        return self.dt.strftime('%H:%M')

    def __eq__(self, other):
        return (self.dt.time() == other.dt.time())

    def __str__(self):
        return self.dt.strftime('%H:%M')
