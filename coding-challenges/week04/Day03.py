class Student:
    def __init__(self, n, r, a, m):
        self.name = n
        self.roll_number = r
        self.age = a
        self.marks = m

def info(self):
    print("The student name is", self.name)

def roll(self):    
    print("Roll number is", self.roll_number)

def age(self):
    print("The student age is", self.age)

def marks(self):
    print("The student marks is", self.marks)

from day004 import Student
if __name__=="__main__":
    name = input("Enter name of student ")
    roll_number = int(input("Enter roll no of student "))
    age = int(input("Enter age of student "))
    marks = int(input("Enter marks of student "))
    student1 = Student(name,roll_number,age,marks)

   
    student1.name()
    student1.roll_number()
    student1.age()
    student1.marks()
