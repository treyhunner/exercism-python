def distance(strand1, strand2):
    return sum(
        n1 != n2
        for n1, n2 in zip(strand1, strand2)
    )
