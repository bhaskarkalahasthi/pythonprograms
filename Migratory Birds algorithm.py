#!/bin/python3

import sys

def migratoryBirds(n, ar):
    # Complete this function
    count=[]
    
    type_of_birds=[1,2,3,4,5]
    for j in range(len(type_of_birds)):
        count1=0
        for i in range(len(ar)):
            if(type_of_birds[j]==ar[i]):
                
                count1=count1+1
        count.append(count1)
    max_value=max(count)
    a=count.index(max_value)
    return type_of_birds[a]
        
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
