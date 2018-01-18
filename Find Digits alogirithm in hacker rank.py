import sys

def findDigits(n,t):
    # Complete this function
    n=str(n)
    count=0
    for i in range(len(n)):
        if(int(n[i])!=0):
            
            if(int(n)%int(n[i])==0):
                count=count+1
    return count
t = int(input().strip())
for a0 in range(t):
n = int(input().strip())
result = findDigits(n,t)
print(result)
