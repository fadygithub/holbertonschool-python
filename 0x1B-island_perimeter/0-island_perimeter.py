#!/usr/bin/python3

"""Island Parameter Task"""


def island_perimeter(grid):
    """This will return the perimeter of the island"""
    x = 0
    nearby = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                x += 1
                if r > 0 and grid[r-1][c] == 1:
                    nearby += 1
                if c > 0 and grid[r][c-1] == 1:
                    nearby += 1
    return x * 4 - nearby * 2
