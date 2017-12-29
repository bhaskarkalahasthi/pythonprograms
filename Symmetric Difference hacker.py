no_inputs=int(input())
user_input1=input()
a=user_input1.split(" ")
if(len(a)==no_inputs):
    b=list(map(int,a))
    b.sort()
    c=set(b)
p=int(input())
user_input2=input()
q=user_input2.split(" ")
if(len(q)==p):
    r=list(map(int,q))
    r.sort()
    s=set(r)
ans1=c.symmetric_difference(s)
b=sorted(list(ans1))
for i in b:
    print(i)
    