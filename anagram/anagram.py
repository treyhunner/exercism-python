def detect_anagrams(word, possible):
    return [
        candidate
        for candidate in possible
        if is_anagram(word, candidate)
    ]


def is_anagram(word1, word2):
    word1, word2 = word1.lower(), word2.lower()
    has_same_letters = sorted(word1) == sorted(word2)
    return has_same_letters and word1 != word2
