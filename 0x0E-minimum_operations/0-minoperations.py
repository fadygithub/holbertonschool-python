#!/usr/bin/python3

"""
minOperations module
"""


def minOperations(n):
    """calculate utilizing the fewest iterations possible"""
    if n <= 1:
        return 0
    div = 2
    res = 0
    while n > 1:
        if n % div == 0:
            n /= div
            res += div
        else:
            div += 1
    return res
