from math import floor, sqrt
from typing import List


def prime_factors(number: int) -> List[int]:
    for n in range(2, floor(sqrt(number) + 1)):
        if number % n == 0:
            return [n, *prime_factors(number//n)]
    return [number] if number != 1 else []
