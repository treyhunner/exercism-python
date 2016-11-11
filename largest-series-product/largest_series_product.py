from functools import partial, reduce
import operator


def window(sequence, length):
    """Return all slices of given length into sequence."""
    return (
        sequence[i:i+length]
        for i in range(len(sequence)-length+1)
    )


product = partial(reduce, operator.mul)


def largest_product(series, substring_length):
    if substring_length < 0:
        raise ValueError("Substring length must be non-negative.")
    digits = [int(d) for d in series]
    return max(
        product(group) if group else 1
        for group in window(digits, substring_length)
    )
