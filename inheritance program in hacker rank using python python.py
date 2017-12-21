class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName, lastName, idNum,scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNum
        self.scores=scores
    

   #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        marks_list=list(self.scores)
        sum=0
        for i in range(len(marks_list)):
            sum=sum+int(marks_list[i])
        percentage=sum/len(marks_list)
        if(percentage>=90 and percentage<=100):
            return "O"
        if(percentage>=80 and percentage<90):
            return "E"
        if(percentage>=70 and percentage<80):
            return "A"
        if(percentage>=55 and percentage<70):
            return "P"
        if(percentage>=40 and percentage<55):
            return "D"
        if(percentage<40):
            return "T"
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())