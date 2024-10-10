#!/usr/bin/python3
"""
a simple module containing a 2D array checking-function
"""
from typing import List,


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    a function checking all the boxes can be opened
    """
    unlocked = [False] * len(boxes)
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
