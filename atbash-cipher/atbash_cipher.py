from itertools import zip_longest
from string import ascii_lowercase as letters


atbash = dict(zip(letters, reversed(letters)))


def decode(string):
    """Return string of each character decoded."""
    return ''.join(
        atbash.get(c, c)
        for c in string.lower()
        if c.isalnum()
    )


def partition(string, n):
    """Return generator of n-letter word groups in string."""
    letter_groups = zip_longest(*[iter(string)]*n, fillvalue='')
    return (
        ''.join(group)
        for group in letter_groups
    )


def encode(string):
    """Decode each letter and group into 5-letter words."""
    return ' '.join(partition(decode(string), 5))
