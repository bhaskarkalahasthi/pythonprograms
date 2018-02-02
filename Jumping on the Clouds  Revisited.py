import sys
def jumpingOnClouds(c, k):
    # Complete this function
    no_of_clouds=len(c)
    i=0
    E=100
    while(i<=no_of_clouds):
        i=i+k
        if(i<=no_of_clouds):
            if(i==no_of_clouds):
                temp=c[0]
            else:
                temp=c[i]
            if(temp==1):
                E=E-3
            else:
                E=E-1
    return E
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c, k)
    print(result)
