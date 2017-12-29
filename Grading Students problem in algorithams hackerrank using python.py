import sys

def solve(grades):
    
    # Complete this function
    result=[]
    student_grades=list(grades)
    for i in range(len(student_grades)):
        if(student_grades[i]%5!=0):
            #In this we check the above 38 marks
            if(student_grades[i]>=38):
                
                #In this find multiple of fives 
                for j in range(1,5,1):
                    if((student_grades[i]+j)%5==0):
                        if((student_grades[i]+j)-student_grades[i]<3):
                            #In this we round the grade
                            grade=student_grades[i]+j
                            result.append(grade)
                        if((student_grades[i]+j)-student_grades[i]==3):
                        
                            result.append(student_grades[i])
                        if((student_grades[i]+j)-student_grades[i]>3):
                            result.append(student_grades[i])
            else:
                result.append(student_grades[i])
        else:
            result.append(student_grades[i])
    return result
    

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


