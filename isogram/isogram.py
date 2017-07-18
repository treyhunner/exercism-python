from string import ascii_lowercase


def is_isogram(word: str) -> bool:
    letters = [
        character
        for character in word.lower()
        if character in ascii_lowercase
    ]
    return len(set(letters)) == len(letters)
