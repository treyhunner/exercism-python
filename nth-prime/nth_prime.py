from itertools import count, islice
from math import floor, sqrt


def is_prime(candidate):
    return all(
        candidate % n != 0
        for n in range(2, ceil(sqrt(candidate))
    ) and 2 <= candidate


def get_primes():
    return (
        number
        for number in count()
        if is_prime(number)
    )


def nth_prime(n):
    return next(islice(get_primes(), n-1, n))
