#!/usr/bin/python3
"""
Module for making change using the minimum number of coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total
    Args:
        coins (list): List of coin denominations available
        total (int): Target amount to make change for
    Returns:
        int: Minimum number of coins needed, -1 if impossible, 0 if total <= 0
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)

    count = 0
    remaining = total

    for coin in coins:
        if coin <= remaining:
            num_coins = remaining // coin
            count += num_coins
            remaining -= num_coins * coin

        if remaining == 0:
            return count

    return -1
