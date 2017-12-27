def split_and_join(line):
    # write your code here
    final_result=line.split(" ")
    res="-".join(final_result)
    return res
line = input()
result = split_and_join(line)
print(result)