#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    max_height=max(ar)
    count=0
    for i in range(len(ar)):
        if(max_height==ar[i]):
            count=count+1
    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
