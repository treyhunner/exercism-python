from typing import Iterable


def is_multiple_of_any(n: int, numbers: Iterable[int]) -> bool:
    return any(
        x != 0 and n % x == 0
        for x in numbers
    )


def sum_of_multiples(limit: int, numbers: Iterable[int]) -> int:
    return sum(
        n
        for n in range(limit)
        if is_multiple_of_any(n, numbers)
    )
