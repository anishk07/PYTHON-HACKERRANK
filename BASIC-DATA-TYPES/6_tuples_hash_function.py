# @author : ANISHK YADAV

"""
Task
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).
"""

# CODE:

N = int(input())

tuplex = tuple(map(int, input().split()))
print(hash(tuplex))
