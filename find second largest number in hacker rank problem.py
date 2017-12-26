list=[]
n=int(input())
user_input=(input())
m=user_input.split(" ")
for i in range(n):
    list.append(int(m[i]))
list1=set(list)
list1.remove(max(list1))
print(max(list1))