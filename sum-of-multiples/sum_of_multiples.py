def is_multiple_of_any(n, numbers):
    return any(
        x != 0 and n % x == 0
        for x in numbers
    )


def sum_of_multiples(limit, numbers):
    return sum(
        n
        for n in range(limit)
        if is_multiple_of_any(n, numbers)
    )
