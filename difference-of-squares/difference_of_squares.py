def sum_of_squares(limit):
    """Return sum of square of all integers up to and including limit."""
    return sum(
        n**2
        for n in range(limit+1)
    )


def square_of_sum(limit):
    """Return square of sum of all integers up to and including limit."""
    return sum(range(limit+1)) ** 2


def difference(limit):
    return square_of_sum(limit) - sum_of_squares(limit)
