from collections import OrderedDict


class OrderedDefaultDict(OrderedDict):
    def __missing__(self, key):
        self[key] = ()
        return self[key]


class School(OrderedDefaultDict):

    @staticmethod
    def __init__(name):
        """Do nothing."""

    def add(self, student, grade):
        self[grade] += (student,)

    def grade(self, grade):
        return self[grade]

    def sort(self):
        return self.items()
