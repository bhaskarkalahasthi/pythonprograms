#!/bin/python3

import sys

def hurdleRace(k, height):
    # Complete this function
    maxheight=max(height)
    res=maxheight-k
    if(res>=0):
        return res
    else:
        return 0
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
height = list(map(int, input().strip().split(' ')))
result = hurdleRace(k, height)
print(result)
