#!/bin/python3

import sys
li=[]

arr = list(map(int, input().strip().split(' ')))
for i in range(len(arr)):
    sum=0
    for j in range(len(arr)):
        if(i!=j):
            sum=sum+arr[j]
    li.append(sum)
print(min(li),max(li))
            
