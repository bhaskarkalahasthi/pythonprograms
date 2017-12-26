n = int(input())
list=[]
m=input()
sp=m.split(" ")
for i in range(n):
    list.append((int(sp[i])))
new_tuple=tuple(list)
result=hash(new_tuple)
print(result)
