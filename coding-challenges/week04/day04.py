class Student:
    def __init__(self, name, roll_number, age, marks):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.marks = marks

    def info(self):
        print("The student name is",
              self.name and "roll number is", self.roll_number)

    def setage(self):
        print("Age of ", self.name, " is ", self.age)

    def setmarks(self):
        print("Marks of ", self.name, " is ", self.marks)

    def display(self):
        print("Name : ", self.name)
        print("RollNumber : ", self.roll_number)
        print("Age : ", self.age)
        print("Marks : ", self.marks)
