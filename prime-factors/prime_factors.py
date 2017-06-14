from math import floor, sqrt


def prime_factors(number):
    for n in range(2, floor(sqrt(number) + 1)):
        if number % n == 0:
            return [n, *prime_factors(number//n)]
    return [number] if number != 1 else []
