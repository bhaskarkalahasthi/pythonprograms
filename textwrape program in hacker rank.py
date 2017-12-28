def wrap(string, max_width):
    res=textwrap.fill(string,max_width)
    return res
string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)