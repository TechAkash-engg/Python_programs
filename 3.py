n=input('Enter the number of students=')
s1=input('Enter the number of subjects=')
class Student:
    def __init__(self):
        self.roll=0
        self.marks=[]
        self.total=0
        self.per=0
        self.grade=""
        
    def setStudent(self):
        self.roll=int(input("Enter Roll number: "))
        print("Enter marks of 5 subjects: ")
        for i in range(5):
            self.marks.append(int(input("Subject "+str(i+1)+": ")))
			
    def calculateTotal(self):
        for x in self.marks:
            self.total+=x
			
    def calculatePercentage(self):
        self.per=self.total/5

		
    def calculateGrade(self):
        if self.per>=90:
            self.grade="A1"
        elif self.per>=80 and self.per<90:
            self.grade="A2"
        elif self.per>=70 and self.per<80:
            self.grade="B1"
        elif self.per>=60 and self.per<70:
            self.grade="B2"
        elif self.per>=50 and self.per<60:
            self.grade="C1"
        elif self.per>=40 and self.per<50:
            self.grade="C2"
        else:
            self.grade="F"
			
			
    def showStudent(self):
        self.calculateTotal()
        self.calculatePercentage()
        self.calculateGrade()
        print(self.roll,"->",self.grade,"\t\t")


def main():
    #Student object
    c=0
    for c in range(5):
        s=Student()
        s.setStudent()
        s.showStudent()

if __name__=="__main__":
    main()
