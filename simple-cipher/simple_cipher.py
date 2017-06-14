from itertools import cycle
from string import ascii_lowercase as ALPHABET


LETTER_A = ALPHABET[0]


LETTERS = {
    letter: ord(letter) - ord(LETTER_A)
    for letter in ALPHABET
}


def shift_letter(letter, amount, reverse):
    if reverse:
        amount = -amount
    number = (LETTERS[letter] + amount) % 26
    return chr(number + ord(LETTER_A))


def encode(message, key, *, reverse=False):
    alpha_characters = (c for c in message.lower() if c in ALPHABET)
    return ''.join(
        shift_letter(letter, LETTERS[amount], reverse)
        for letter, amount in zip(alpha_characters, cycle(key))
    )


def decode(message, key):
    return encode(message, key, reverse=True)


class Cipher:
    """This class API is pretty silly..."""
    def __init__(self, key='d' * 1000):
        if any(c not in ALPHABET for c in key):
            raise ValueError
        self.key = key

    def encode(self, message):
        return encode(message, self.key)

    def decode(self, message):
        return decode(message, self.key)


Caesar = Cipher
