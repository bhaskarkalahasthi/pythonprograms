#!/bin/python3
import sys
def designerPdfViewer(h, word):
    # Complete this function
    res=[]
    alpha_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(word)):
        temp=alpha_list.index(word[i])
        a=h[temp]
        res.append(a)
    height=max(res)
    t=len(word)
    area=t*height*1
    return area
h = list(map(int, input().strip().split(' ')))
word = input().strip()
result = designerPdfViewer(h, word)
print(result)
