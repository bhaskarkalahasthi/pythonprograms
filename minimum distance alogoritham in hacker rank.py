#!/bin/python3
import sys
def minimumDistances(a):
    # Complete this function
    distance=[]
    for i in range(len(a)):
        for k in range(len(a)):
            if(i!=k):
                if(a[i]==a[k]):
                    res=abs(i-k)
                    distance.append(res)
    if(len(distance)>0):
        return min(distance)
    else:
        return -1
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = minimumDistances(a)
print(result)
