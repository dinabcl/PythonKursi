class Person:
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name}, and i am {self.age} years old.")

personi1 = Person("Elmedina",18)
personi2 = Person("Gojo", 26)

personi1.greet()
personi2.greet()