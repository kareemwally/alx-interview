#!/usr/bin/python3
"""
simple module to solve the N queens problems
"""
import sys


def print_usage_and_exit():
    """
    """
    print("Usage: nqueens N")
    sys.exit(1)


def solve_nqueens(n):
    """
    solving function for N queens
    """
    solutions = []
    board = [-1] * n
    backtrack(board, 0, solutions, n)
    return solutions


def backtrack(board, row, solutions, n):
    """
    backtracking
    """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
    else:
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1, solutions, n)
                board[row] = -1


def is_safe(board, row, col):
    """
    chscking safety
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def main():
    """
    the main functio to call all other function in module
    """
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
