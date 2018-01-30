#!/bin/python3
import sys
def kangaroo(x1, v1, x2, v2):
    # Complete this function
    kangaroo1=x1
    kangaroo2=x2
    for i in range(10000):
        kangaroo1=kangaroo1+v1
        kangaroo2=kangaroo2+v2
        if(kangaroo1==kangaroo2):
            return "YES"
        if(i==9999):
            if(kangaroo1!=kangaroo2):
                return "NO"
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
