#!/bin/python3
import sys
def maximizingXor(l, r):
    # Complete this function
    min_value=[]
    for i in range(l,r+1):
        for j in range(i,r+1):
            min_value.append(i^j)
    return max(min_value)
l = int(input().strip())
r = int(input().strip())
result = maximizingXor(l, r)
print(result)
