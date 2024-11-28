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

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
