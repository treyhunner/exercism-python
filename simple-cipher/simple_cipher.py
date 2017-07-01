from itertools import cycle
from string import ascii_lowercase as ALPHABET


LETTER_A = ALPHABET[0]


LETTERS = {
    letter: ord(letter) - ord(LETTER_A)
    for letter in ALPHABET
}


def shift_letter(letter: str, amount: int, reverse: bool) -> str:
    if reverse:
        amount = -amount
    number = (LETTERS[letter] + amount) % 26
    return chr(number + ord(LETTER_A))


def encode(message: str, key: str, *, reverse: bool = False) -> str:
    alpha_characters = (
        char
        for char in message.lower()
        if char in ALPHABET
    )
    return ''.join(
        shift_letter(letter, LETTERS[amount], reverse)
        for letter, amount in zip(alpha_characters, cycle(key))
    )


def decode(message: str, key: str) -> str:
    return encode(message, key, reverse=True)


class Cipher:
    """This class API is pretty silly..."""
    def __init__(self, key: str = 'd' * 1000) -> None:
        if any(c not in ALPHABET for c in key):
            raise ValueError
        self.key = key

    def encode(self, message: str) -> str:
        return encode(message, self.key)

    def decode(self, message: str) -> str:
        return decode(message, self.key)


Caesar = Cipher
