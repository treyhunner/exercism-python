def saddle_points(matrix):
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Rows have different lengths.")
    rows, columns = matrix, list(zip(*matrix))
    return {
        (x, y)
        for x, row in enumerate(matrix)
        for y, value in enumerate(row)
        if value == max(rows[x])
        and value == min(columns[y])
    }
