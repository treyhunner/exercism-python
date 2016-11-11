MAGNITUDES = [
    (1_000_000_000, 'billion'),
    (1_000_000, 'million'),
    (1000, 'thousand'),
]

VALUES = {
    90: 'ninety',
    80: 'eighty',
    70: 'seventy',
    60: 'sixty',
    50: 'fifty',
    40: 'forty',
    30: 'thirty',
    20: 'twenty',
    19: 'nineteen',
    18: 'eighteen',
    17: 'seventeen',
    16: 'sixteen',
    15: 'fifteen',
    14: 'fourteen',
    13: 'thirteen',
    12: 'twelve',
    11: 'eleven',
    10: 'ten',
    9: 'nine',
    8: 'eight',
    7: 'seven',
    6: 'six',
    5: 'five',
    4: 'four',
    3: 'three',
    2: 'two',
    1: 'one',
}


def ten_words(number):
    """Translate number from 1 to 99 to words."""
    if number in VALUES:
        yield VALUES[number]
    else:
        times, number = divmod(number, 10)
        yield VALUES[times*10]+'-'+VALUES[number]


def hundred_words(number, force_and=False):
    """Translate number from 1 to 999 to words."""
    times, number = divmod(number, 100)
    if times:
        yield VALUES[times]
        yield 'hundred'
    if number:
        if times or force_and:
            yield 'and'
        yield from ten_words(number)


def say(number):
    if not (0 <= number < 10**12):
        raise AttributeError
    words = []
    for scale, word in MAGNITUDES:
        times, number = divmod(number, scale)
        if times:
            words += hundred_words(times)
            words.append(word)
    if number:
        words += hundred_words(number, force_and=bool(words))
    elif not words:
        words.append('zero')
    return ' '.join(words)
