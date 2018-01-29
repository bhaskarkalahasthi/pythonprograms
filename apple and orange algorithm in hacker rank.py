#!/bin/python3

import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Complete this function
    count=0
    count_oranges=0
    for i in range(len(apples)):
        if(s<=a+apples[i]<=t):
            count=count+1
    print(count)
    for j in range(len(oranges)):
        if(s<=b+oranges[j]<=t):
            count_oranges=count_oranges+1
    print(count_oranges)
s, t = input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = input().strip().split(' ')
m, n = [int(m), int(n)]
apple = list(map(int, input().strip().split(' ')))
orange = list(map(int, input().strip().split(' ')))
countApplesAndOranges(s, t, a, b, apple, orange)
