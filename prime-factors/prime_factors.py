from itertools import count
import math


def prime_factors(number):
    limit = math.ceil(math.sqrt(number))+1
    for n in range(2, limit):
        if number % n == 0:
            return [n, *prime_factors(number//n)]
    return [number] if number != 1 else []
