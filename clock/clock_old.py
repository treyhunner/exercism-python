from functools import total_ordering


#@total_ordering
class Clock:

    def __init__(self, hour, minute):
        total_minutes = hour * 60 + minute
        self.hour = (total_minutes // 60) % 24
        self.minute = total_minutes % 60

    def __eq__(self, other):
        return (self.hour, self.minute) == (other.hour, other.minute)

    def __lt__(self, other):
        return (self.hour, self.minute) < (other.hour, other.minute)

    def __add__(self, other):
        if isinstance(other, int):
            hour, minute = self.hour, self.minute + other
        else:
            hour, minute = self.hour + other.hour, self.minute + other.minute
        return self.__class__(hour, minute)

    add = __add__  # hm?

    def __str__(self):
        return f"{self.hour:0>2}:{self.minute:0>2}"
