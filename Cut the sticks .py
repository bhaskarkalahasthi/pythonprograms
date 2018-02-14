#!/bin/python3
import sys
def cutTheSticks(arr):
    res=[]
    a=len(arr)
    while(a>0):
        print(a)
        res.append(len(arr))
        min_value=min(arr)
        for i in range(a):
            arr[i]=arr[i]-min_value
        for j in range(a):
            if(arr[j]==0):
                arr.remove(arr[j])
        print(len(arr))
        a=len(a)
    return res
n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
result = cutTheSticks(arr)
print ("\n".join(map(str, result)))