#!/usr/bin/python3
"""
simple module to soleve the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in the grid.
    Args:
        grid (list of list of int): A rectangular grid where
        1 => land and 0 => water.
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2
    return perimeter
