class Student:
    schoolName = "Digital School"

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Elmedina", 17, "Python")
student2 = Student("Dina", 16, "React Native")
print(student1.schoolName)
print(student2.name)
print(student1.course)