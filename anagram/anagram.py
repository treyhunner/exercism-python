from typing import List


def detect_anagrams(word: str, possible: List[str]) -> List[str]:
    return [
        candidate
        for candidate in possible
        if is_anagram(word, candidate)
    ]


def is_anagram(word1: str, word2: str) -> bool:
    word1, word2 = word1.lower(), word2.lower()
    has_same_letters = sorted(word1) == sorted(word2)
    is_same_word = word1 != word2
    return has_same_letters and is_same_word
