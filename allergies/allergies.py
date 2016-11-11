from collections import UserList


class Allergies(UserList):

    """The API of this object feels a bit unpythonic."""

    items = [
        'eggs',
        'peanuts',
        'shellfish',
        'strawberries',
        'tomatoes',
        'chocolate',
        'pollen',
        'cats',
    ]

    def __init__(self, number):
        self.data = [
            item
            for i, item in enumerate(self.items)
            if number & (1 << i)
        ]

    @property
    def lst(self):
        """Using `lst` makes for a slightly silly API in Python."""
        return list(self)

    def is_allergic_to(self, item):
        """This method isn't really needed when there's containment."""
        return item in self
