user_input=int(input())
list_of_values=input()
list_of_values1=set(map(int,list_of_values.split(" ")))
for i in range(int(input())):
    user_input_commands=input().split(" ")
    if("pop"==user_input_commands[0]):
        list_of_values1.pop()
    if("remove"==user_input_commands[0]):
        if int(user_input_commands[1]) in list_of_values1:
            list_of_values1.remove(int(user_input_commands[1]))
    if("discard"==user_input_commands[0]):
        if int(user_input_commands[1]) in list_of_values1:
            list_of_values1.discard(int(user_input_commands[1]))
print(sum(list(list_of_values1)))