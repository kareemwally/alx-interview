#!/usr/bin/python3
"""
simple module to solve the prime game
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game across multiple rounds
    Args:
        x (int): number of rounds
        nums (list): array of n for each round
    Returns:
        str: name of the winner (Maria/Ben) or None if tie
    """
    if not nums or x < 1:
        return None

    def get_primes_up_to(n):
        """Generate a list of primes up to n using Sieve of Eratosthenes"""
        if n < 2:
            return []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False

        return [i for i in range(2, n + 1) if sieve[i]]

    def play_round(n):
        """
        Simulate a single round of the game
        Returns True if Maria wins, False if Ben wins
        """
        if n < 2:
            return False

        primes = get_primes_up_to(n)
        if not primes:
            return False

        moves = len(primes)
        return moves % 2 == 1

    maria_wins = sum(1 for n in nums[:x] if play_round(n))
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
