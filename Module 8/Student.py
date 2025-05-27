class Student:
    school_name = "Digital School"
 # student_name = "Student"
#student_1 = Student()
#print(student_1.school_name)
#print(student_1.student_name)

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student_1 = Student("Alice", 16, "Python")
print(student_1.course)