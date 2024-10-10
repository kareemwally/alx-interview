#!/usr/bin/python3
"""
A simple module to check all oxes can be opened
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Function to determine if all boxes can be unlocked.
    """
    mySet = set()
    mySet.update(boxes[0])

    for i in range(1, len(boxes)):
        if i in mySet:
            mySet.update(boxes[i])

    return len(mySet) == len(boxes) - 1
