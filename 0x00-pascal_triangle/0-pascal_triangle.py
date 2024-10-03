#!/usr/bin/python3
def pascal_triangle(n: int) -> [[int]]:
    """
    using nested loops, we create the n-rows , 1:n columns matrix
    """
    if int(n) != n:
        raise TypeError("n must be a poitive integer")

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
