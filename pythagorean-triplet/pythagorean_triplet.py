from math import floor, gcd, sqrt


def get_factor_pairs(number):
    return (
        (n, number//n)
        for n in range(1, floor(sqrt(number))+1)
        if number % n == 0
    )


def are_coprime(a, b):
    return gcd(a, b) == 1


def is_triplet(triplet):
    a, b, c = sorted(triplet)
    return a**2 + b**2 == c**2


def triplets_in_range(start, stop):
    primitives = (
        triplet
        for n in range(2, stop, 2)
        for triplet in primitive_triplets(n)
    )
    all_triplets = (
        (k*a, k*b, k*c)
        for (a, b, c) in primitives
        for k in range(1, stop//max(a, b, c) + 1)
    )
    return {
        (a, b, c)
        for (a, b, c) in all_triplets
        if start <= min(a, b, c)
        and max(a, b, c) <= stop
    }


def primitive_triplet(n, m):
    a = m**2 - n**2
    b = 2 * n * m
    c = m**2 + n**2
    return tuple(sorted((a, b, c)))


def primitive_triplets(b):
    if b % 2 != 0:
        raise ValueError("{} is not even".format(b))
    return {
        primitive_triplet(n, m)
        for n, m in get_factor_pairs(b//2)
        if are_coprime(n, m)
        and (n % 2 == 0 or m % 2 == 0)
    }
