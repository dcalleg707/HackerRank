class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = int(idNumber)
        self.scores = scores
    

    def calculate(self):
        nota = 0
        for i in self.scores:
            nota += int(i)
        nota=(nota/len(self.scores))
        if nota>=90:
            return "O"
        elif nota>=80:
            return "E"
        elif nota>=70:
            return "A"
        elif nota>=55:
            return "P"
        elif nota>=40:
            return "D"
        elif nota<40:
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
