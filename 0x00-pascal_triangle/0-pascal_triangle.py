#!/usr/bin/python3
def matrix(n):
    """making a full n-rows with 1:n columns matrix all elements =1"""
    res = []
    for i in range(n):
        res.append([1 for _ in range(i + 1)])
    return res


def pascal_triangle(n):
    """
    pascal traingle is a true wonder in the mathmatics field

    """
    if int(n) != n:
        raise TypeError("n must be an integer")
    
    mat = matrix(n)
    if len(mat) <= 2:
        return mat
    

    for i in range(2, n):
        for j in range(1,len(mat[i]) - 1):
            mat[i][j] = mat[i -1 ][j - 1] + mat [i - 1] [j]
    
    return mat
