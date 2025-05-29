class Animal:
    def __init__(self,name):#shembulli per nje konstruktor dhe nje variable e cila po inicohet per kete klase
        self.name=name

    def sound(self):
        print("Some generic animal sound")
    def description(self):
        print(f"This is an animal named {self.name}")

class Dog(Animal):
    def __init__(self , breed, name):#ketu eshte konstruktori i klases dhe ketu jan variablat e klases
        self.breed = breed #variabla qe vlen vetem per kete klases
        super().__init__(name) #ketu thirret konstruktori i superklasese

    def sound(self):
        print("Woof Woof")

    def description(self):
        super().description()
        print(f"Breed: {self.breed}")

class Cat(Animal):
    def __init__(self, color, name):  # ketu eshte konstruktori i klases dhe ketu jan variablat e klases
        self.color = color  # variabla qe vlen vetem per kete klases
        super().__init__(name)  # ketu thirret konstruktori i superklasese

    def sound(self):
        print("Meow Meow")

    def description(self):
        super().description()
        print(f"Color: {self.color}")

rex=Dog("Golden Retriever","Rex" )
rex.sound()
rex.description()

tom = Cat("Orange", "Tom")
tom.sound()
tom.description()