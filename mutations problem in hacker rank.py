def mutate_string(string, position, character):
    string1=string
    result=list(string1)
    result[position]=character
    string1=''.join(result)
    return string1
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)