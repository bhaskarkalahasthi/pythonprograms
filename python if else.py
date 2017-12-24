n=int(input())
m=n%2
if(m==0):
    if(2<=n<=5 or n>20 ):
        print("Not Weird")
    else:
        print("Weird")
if(m!=0):
    print("Weird")
    