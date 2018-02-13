#!/bin/python3
import sys
def taumBday(b, w, x, y, z):
    # Complete this function
    res=[]
    cost=b*x+w*y
    res.append(cost)
    cost=(b*(y+z))+(w*y)
    res.append(cost)
    cost=(b*x)+(w*(x+z))
    res.append(cost)
    min_val=min(res)
    res=[]
    return min_val
t = int(input().strip())
for a0 in range(t):
    b, w = input().strip().split(' ')
    b, w = [int(b), int(w)]
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]
    result = taumBday(b, w, x, y, z)
    print(result)
