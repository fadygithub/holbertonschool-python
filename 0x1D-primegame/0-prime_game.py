#!/usr/bin/python3

"""isWinner Module"""


def isWinner(x, nums):
    """Prime numbers game"""
    if x < 0 or nums[-1] < 1:
        return None
    Maria_score = 0
    Ben_score = 0
    prime_number = [False] * 100001
    p = []
    for i in range(2, 100001):
        if not prime_number[i]:
            p.append(i)
            for j in range(i, 100001, i):
                prime_number[j] = True

    l = 0
    for a0 in range(x):
        n = nums[l]
        num = 0
        for x in range(100001):
            if x >= len(p) or p[x] > n:
                break
            num += 1
        l += 1
        if (['Maria', 'Ben'][(num % 2) ^ 1]) == "Maria":
            Maria_score += 1
        else:
            Ben_score += 1
    if Maria_score > Ben_score:
        return "Maria"
    else:
        return "Ben"
