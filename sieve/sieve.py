from math import ceil, sqrt


def sieve(limit):
    # Start with 0 & 1 non-prime and everything else assumed prime
    primality = [False, False] + [True] * (limit - 1)
    for n in range(2, ceil(sqrt(limit))):
        if primality[n]:
            # All multiples of n are non-prime
            primality[n*2::n] = [False] * len(primality[n*2::n])
    return [
        n
        for n, is_prime in enumerate(primality)
        if is_prime
    ]
