#!/bin/python3
import sys
def lonelyinteger(a):
    # Complete this function
    for i in range(len(a)):
        count=a.count(a[i])
        if(count==1):
            return a[i]
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonelyinteger(a)
print(result)
