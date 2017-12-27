n =int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
  
    
query_name = input()
res=student_marks[query_name]
n=len(res) 
result=float(sum(res)/n)
print("{:.2f}".format(result))
    
    