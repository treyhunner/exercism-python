from string import ascii_lowercase


def is_pangram(sentence: str) -> bool:
    """Return True if sentence contains all English letters."""
    return set(ascii_lowercase) <= set(sentence.lower())
