list=[]
n=int(input())
for i in range(n):
    user_input=input()
    splited=user_input.split(" ")
    if("insert"==splited[0]):
        list.insert(int(splited[1]),int(splited[2]))
   
    if("print"==splited[0]):
        print(list)
    if("remove"==splited[0]):
        list.remove(int(splited[1]))
    if("append"==splited[0]):
        list.append(int(splited[1]))
    if("sort"==splited[0]):
        list.sort()
    if("pop"==splited[0]):
        list.pop()
    if("reverse"==splited[0]):
        list.reverse()