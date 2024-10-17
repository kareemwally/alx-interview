#!/usr/bin/python3
"""
a simple module containing a function returning
the least number of operations using DP
"""


def minOperations(n: int) -> int:
    """
    dividing the main number into a set of smaller numbers
    """
    res = 1
    i = 1
    sep = 1
    while i < n:
        if (n % i == 0 and i != 1):
            sep = i * 2
            i += sep
            res += 2
        else:
            res += 1
            i += sep
    return res
