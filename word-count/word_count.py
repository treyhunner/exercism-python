from collections import Counter
import re


WORD_RE = re.compile(r'[^\W_]+')


def word_count(phrase):
    words = WORD_RE.findall(phrase.lower())
    return Counter(words)
