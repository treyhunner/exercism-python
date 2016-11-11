from itertools import dropwhile
from random import choice
from string import ascii_uppercase as letters, digits


class Robot:

    used_names = set()

    def __init__(self):
        self.reset()

    @staticmethod
    def generate_names():
        while True:
            alphabets = [letters] * 2 + [digits] * 3
            yield "".join(
                choice(alphabet)
                for alphabet in alphabets
            )

    def get_random_name(self):
        def name_used(name): return name in self.used_names
        names = self.generate_names()
        return next(dropwhile(name_used, names))

    def reset(self):
        self.name = self.get_random_name()
        self.used_names.add(self.name)
