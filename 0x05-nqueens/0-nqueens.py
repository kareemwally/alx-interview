#!/usr/bin/python3
"""
simple module to solve the N queens problems
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen on board[row][col].
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and print all possible solutions.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    for solution in solutions:
        print(solution)


def solve_nqueens_util(board, col, n, solutions):
    """
    Recursive utility function to solve the N Queens problem.
    """
    if col == n:
        solutions.append([[row, col] for row, col in enumerate(board)])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n, solutions)
            board[i][col] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
