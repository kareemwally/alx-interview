#!/usr/bin/python3
"""
simple module to solve the prime game
"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game played x rounds.

    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers representing
    the upper limit of the set for each round.

    Returns:
    str: The name of the player that won the most rounds
    ("Maria" or "Ben").
         If the winner cannot be determined, returns None.
    """
    def sieve(n):
        """
        Generates a list of prime numbers up to
        n using the Sieve of Eratosthenes.

        Parameters:
        n (int): The upper limit to generate prime numbers.

        Returns:
        list: A list of prime numbers up to n.
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if (is_prime[p] is True):
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_numbers

    def play_game(n):
        """
        Simulates the prime game for a given:
        n and counts the number of moves.

        Parameters:
        n (int): The upper limit of the set for the game.

        Returns:
        int: The number of moves made in the game.
        """
        primes = sieve(n)
        moves = 0
        while primes:
            prime = primes[0]
            primes = [p for p in primes if p % prime != 0]
            moves += 1
        return moves

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = play_game(n)
        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
