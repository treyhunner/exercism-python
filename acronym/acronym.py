import re


WORDS_RE = re.compile(r'(?<=[a-z])[A-Z]|(?<=\b)\w')


def abbreviate(string: str) -> str:
    return ''.join(
        first_letter
        for first_letter, *other_letters in WORDS_RE.findall(string)
    ).upper()
