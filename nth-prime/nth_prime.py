from itertools import count, islice
from math import floor, sqrt
from typing import Iterator


def is_prime(candidate: int) -> bool:
    return all(
        candidate % n != 0
        for n in range(2, floor(sqrt(candidate)+1))
    ) and 2 <= candidate


def get_primes() -> Iterator[int]:
    return (
        number
        for number in count()
        if is_prime(number)
    )


def nth_prime(n: int) -> int:
    return next(islice(get_primes(), n-1, n))
