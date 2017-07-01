import re
from typing import Match


def substitute_word(match: Match[str]) -> str:
    if re.search(r'^[xy][^aeiou]', match.group(1)):
        return match.group(0) + "ay"
    else:
        return "{1}{0}ay".format(*match.groups())


def translate(sentence: str) -> str:
    PIG_LATIN_RE = re.compile(
        r'''
        \b
        (
            [^aeiou\s]*
            (?: (?<=q)u )?
        )
        (\w*)
        \b
        ''', re.VERBOSE)
    return PIG_LATIN_RE.sub(substitute_word, sentence)
