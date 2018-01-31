#!/bin/python3
import sys
def viralAdvertising(n):
    # Complete this function
    persons=5
    sum=0
    while(n>0):
        res=int(persons/2)
        sum=sum+res
        persons=res*3
        n=n-1
    return sum
n = int(input().strip())
result = viralAdvertising(n)
print(result)
