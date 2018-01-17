#!/bin/python3
import sys
def beautifulDays(i, j, k):
    # Complete this function
    li=[]
    for i in range(i,j+1):
        #print(i)
        a=i
        res=0
        while(a>0):
            rem=a%10
            res=rem+res*10
            a=a//10
        #print(i)
        #print(res)
        whole=abs(i-res)%k
        #print(whole)
        if(whole==0):
            li.append(i)
    return len(li)
i, j, k = input().strip().split(' ')
i, j, k = [int(i), int(j), int(k)]
result = beautifulDays(i, j, k)
print(result)
