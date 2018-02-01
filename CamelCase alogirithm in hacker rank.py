#!/bin/python3
import sys
def camelcase(s):
    # Complete this function
    a=''.join( ' '+x if 'A' <= x <= 'Z' else x for x in s )
    b=a.split(" ")
    return len(b)
s = input().strip()
result = camelcase(s)
print(result)
