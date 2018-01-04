import sys

def breakingRecords(score):
    # Complete this function
    count=0
    count1=0
    res=[]
    a=score[0]
    b=score[0]
    for i in range(len(score)-1):
        if(a<score[i+1]):
            a=score[i+1]
            count=count+1
        if(b>score[i+1]):
            b=score[i+1]
            count1=count1+1
    res.append(count)
    res.append(count1)
    return res

n = int(input().strip())
score = list(map(int, input().strip().split(' ')))
result = breakingRecords(score)
print (" ".join(map(str, result)))

