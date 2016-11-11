def slices(digits, n):
    if not (0 < n <= len(digits)):
        raise ValueError("Slice length invalid.")
    substrings = zip(*(
        (int(d) for d in digits[i:])
        for i in range(n)
    ))
    return [
        [int(d) for d in substring]
        for substring in substrings
    ]
