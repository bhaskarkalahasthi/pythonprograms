#!/bin/python3

import sys

def serviceLane(n, cases,width):
    # Complete this function
    res=[]
    #print("ayhdgcyufgewqfgef")
    #print(cases)
    #print(width)
    for i in range(len(cases)):
        a=cases[i][0]
        b=cases[i][1]
        #print((width[a:b+1]))
        min_value=min(width[a:b+1])
        res.append(min_value)
    return res
if __name__ == "__main__":
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    width = list(map(int, input().strip().split(' ')))
    cases = []
    for cases_i in range(t):
        cases_t = [int(cases_temp) for cases_temp in input().strip().split(' ')]
        cases.append(cases_t)
    result = serviceLane(n, cases,width)
    print ("\n".join(map(str, result)))
