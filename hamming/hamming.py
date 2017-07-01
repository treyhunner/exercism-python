def distance(strand1: str, strand2: str) -> int:
    return sum(
        n1 != n2
        for n1, n2 in zip(strand1, strand2)
    )
