from itertools import combinations_with_replacement
user_input=input("")
splited=user_input.split(" ")
result=list(combinations_with_replacement(sorted(splited[0]),int(splited[1])))
for i in range(len(result)):
    print("".join(result[i]))
