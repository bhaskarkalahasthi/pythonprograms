#!/bin/python3

import sys

def angryProfessor(k, a):
    count=0
    # Complete this function
    for i in range(len(a)):
        if(a[i]<=0):
            count=count+1
    if(count>=k):
        return "NO"
    else:
        return "YES"
t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = list(map(int, input().strip().split(' ')))
    result = angryProfessor(k, a)
    print(result)
