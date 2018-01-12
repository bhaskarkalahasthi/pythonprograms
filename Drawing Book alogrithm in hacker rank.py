import sys

def solve(n, p):
    # Complete this function
    count=0
    a=1
    count1=0
    for i in range(1,n+1):
        if(a==i):
            
            if(i==p):
                count=0
                break
        if(i%2==0):
            count=count+1;
            if(i+1==p or i==p):
                break
    for j in range(n,n>0,-1):
        #print(j)
        if(n==p):
            count1=0
        if(n%2==0):
            
            if(j%2!=0):
                count1=count1+1
                if(j==p or j-1==p):
                    break
        if(n%2!=0):
            if(j%2==0):
                
                count1=count1+1;
            if(j-1==p or j==p):
                
                break
            
    #print(count,count1)
    if(count1==count):
        return count
    if(count1>count):
        return count
    else:
        return count1
        
   
        

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
