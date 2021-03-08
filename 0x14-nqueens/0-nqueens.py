#!/usr/bin/python3
"""
    0-nqueens.py Task
"""
import sys


def format(board):
    """Print board"""
    r = []
    for x in range(len(board)):
        colIdx = board[x].index(1)
        r.append([x, colIdx])
    print(r)


def is_Valid(board, column, row, n):
    """We check if the location is a valid queen"""
    # Check the previous columns
    for x in range(column):
        if board[row][x] == 1:
            return False
    # Check for the upper diagonal
    r = row
    c = column
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1
    # Check for the lower diagonal
    r = row
    c = column
    while r < n and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1
    return True


def Queens(board, column, n):
    """Place our queen in all the
     positions of the board recursivly"""
    flag = False
    if column == n:
        format(board)
        return True
    for row in range(0, n):
        if is_Valid(board, column, row, n):
            board[row][column] = 1
            flag = Queens(board, column + 1, n) or flag
            board[row][column] = 0
    return flag


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
    board = [[0 for i in range(n)]for j in range(n)]
    nQueens(board, 0, n)
