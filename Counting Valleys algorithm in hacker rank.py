#!/bin/python3
import sys
def countingValleys(n, s):
    # Complete this function
    count=0
    count1=0
    for i in range(len(s)):
        #print(s[i])
        if(s[i]=="U"):
            ++count
        if(s[i]=="D"):
            --count
        if(count==0 and s[i]=="U"):
            ++count1
    return count1
n = int(input().strip())
s = input().strip()
result = countingValleys(n, s)
print(result)
