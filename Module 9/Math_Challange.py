import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


class Trianlge(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Parallelogram(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.height * self.base

rrethi = Circle(2)
drejtekendshi = Rectangle(2,4)
trekendeshi = Trianlge(2,4)
paralelogrami = Parallelogram(3,4)


print("Siperfaqja e rrethit eshte: ", rrethi.area())
print("Siperfaqja e drejtekendshi eshte: ", drejtekendshi.area())
print("Siperfaqja e trekendeshi eshte: ", trekendeshi.area())
print("Siperfaqja e paralelogrami eshte: ", paralelogrami.area())