import re


WORDS_RE = re.compile(r'(?<=[a-z])[A-Z]|(?<=\b)\w')


def abbreviate(string):
    return ''.join(
        word[0]
        for word in WORDS_RE.findall(string)
    ).upper()
