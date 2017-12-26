list=[]
list1=[]
n=int(input())
for i in range(n):
    
    
    
    name=input()
    marks=input()
    list1.append([name,float(marks)])
    list.append(float(marks))
list=set(list)
A=min(list)
list.remove(A)
value=min(list)
list1.sort()
for j in range(len(list1)):
    if(value==list1[j][1]):
        print(list1[j][0])
    

