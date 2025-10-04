class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def greet(self):
        print(f"Hello, I am {self.name} and i am {self.age} years old")

person1 = Person("Alice",38)
person2 = Person("Bob",24)

person1.greet()
person2.greet()