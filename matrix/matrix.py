def matrix_from_string(string):
    """Convert rows of numbers to list of lists."""
    return [
        [int(x) for x in row.split()]
        for row in string.splitlines()
    ]


def transpose_matrix(matrix):
    """Return a transposed version of given list of lists."""
    return [
        list(column)
        for column in zip(*matrix)
    ]


class Matrix:
    """Turn a string into a matrix-like thing."""
    def __init__(self, string):
        matrix = matrix_from_string(string)
        transpose = transpose_matrix(matrix)
        self.rows, self.columns = matrix, transpose
