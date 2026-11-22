class Student:

    school_name = "Institute of Technology of Cambodia"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self, major):
        greeting = "\nHello, my major is"

        print(f"{greeting} {major}")
        print(f"My name is {self.name}, I am {self.age} years old.")
        print(f"I studt at {Student.school_name}\n")

student1 = Student("Nita", 19)
student2 = Student("Piseth", 20)

student1.introduce("Applied Mathematics and Statistics")
student2.introduce("Python Progranmming")

print(f"From Class name directly: {Student.school_name}")
print(f"From Student 1 object: {Student.school_name}")
print(f"From Student 2 object: {Student.school_name}")