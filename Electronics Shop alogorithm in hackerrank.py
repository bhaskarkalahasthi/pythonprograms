#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    cost_combinations=[]
    res=[]
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            sum=keyboards[i]+drives[j]
            cost_combinations.append(sum)
    a=cost_combinations[0]
    for k in range(len(cost_combinations)):
        if(cost_combinations[k]<=s):
            a=cost_combinations[k]
            res.append(a)
    
    #print(max(res))
    if(len(res)>0):
        
        a=max(res)
        if(a<=s):
            return a
        else:
            return "-1"
    else:
        return "-1"
                
s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
