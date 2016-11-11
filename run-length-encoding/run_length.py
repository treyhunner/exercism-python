import re


REPEATS_RE = re.compile(r'(.)\1*')
NUMBERS_RE = re.compile(r'(\d+)(.)')


def to_numbers(match):
    length = len(match.group(0))
    return (
        str(length) + match.group(1)
        if length > 1
        else match.group(1)
    )


def from_numbers(match):
    return int(match.group(1)) * match.group(2)


def encode(string):
    return REPEATS_RE.sub(to_numbers, string)


def decode(string):
    return NUMBERS_RE.sub(from_numbers, string)
