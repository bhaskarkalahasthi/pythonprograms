def capitalize(string):
    temp1=string.split(" ")
    for i in range(len(temp1)):
        temp1[i]=temp1[i].capitalize()
    
    return " ".join(temp1)

string = input()
capitalized_string = capitalize(string)
print(capitalized_string)