import sys

def sockMerchant(n, ar):
    # Complete this function
    set1=list(set(ar))
    list_count=[]
    res=0
    for i in range(len(set1)):
        count=0
        for j in range(len(ar)):
            if(set1[i]==ar[j]):
                count=count+1
        list_count.append(count)
    for k in range(len(list_count)):
        while(list_count[k]>=2):
            res=res+1
            list_count[k]=list_count[k]-2
            
    return res 

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
