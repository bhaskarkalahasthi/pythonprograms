#!/bin/python3
import sys
def permutationEquation(p):
    # Complete this function
    result=[]
    for i in range(1,n+1):
        a=p.index(i)
        a=a+1
        b=p.index(a)
        b=b+1
        result.append(b)
    return result
n = int(input().strip())
p = list(map(int, input().strip().split(' ')))
result = permutationEquation(p)
print ("\n".join(map(str, result)))


