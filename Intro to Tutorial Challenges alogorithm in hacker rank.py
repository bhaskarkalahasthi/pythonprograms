import sys
def introTutorial(V, arr):
    # Complete this function
    for i in range(len(arr)):
        if(V==arr[i]):
            a=i
            break
    return a  
V = int(input().strip())
n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
result = introTutorial(V, arr)
print(result)
