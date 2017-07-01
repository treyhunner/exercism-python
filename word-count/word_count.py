import re
from typing import Counter


WORD_RE = re.compile(r'[^\W_]+')


def word_count(phrase: str) -> Counter[str]:
    words = WORD_RE.findall(phrase.lower())
    return Counter(words)
