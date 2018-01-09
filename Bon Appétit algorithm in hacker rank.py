import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    #print(b)
    bon=ar[k]
    #print(bon)
    ar.remove(bon)
    total=sum(ar)
    #print(total)
    if(total//2==b):
        return "Bon Appetit"
    else:
        return abs(total//2-b)
        
        
    
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
