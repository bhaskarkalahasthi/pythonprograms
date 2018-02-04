#!/bin/python3
import sys
def equalizeArray(arr):
    # Complete this function
    res=[]
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if(arr[i]==arr[j]):
                count=count+1
        res.append(count)
    max_value=max(res)
    return len(arr)-max_value
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
