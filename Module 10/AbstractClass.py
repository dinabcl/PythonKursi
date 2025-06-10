from abc import ABC

class ClassName(ABC):#this is the final defiiniton of an abstract class
    pass

class Shape(ABC):#kls abstrakte
    #metod abstrakte
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius


class Square(Shape):
    def __init__(self, brinja):
        self.brinja = brinja

    def area(self):
        return 2**self.brinja

#objektet per keto dy klasa
circle_1 = Circle(7)
square_1 = Square(18)

print(circle_1.area())
print(square_1.area())

#klasat abstrajte mund te ken edghe metoda te thjeshta edhe abstrakte
#interfaces jan kalasa abstrakte qe kan vetem metoda abstrakte
#kena kriju pahiri interface
