#!/usr/bin/python3
"""
a simple module containing a function returning
the least number of operations using DP
"""


def minOperations(n: int) -> int:
    """
    dividing the main number into a set of smaller numbers
    """
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
