class Dog:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: Ham")


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: Mjau")


class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: Ciu")

qeni = Dog("Max")
macja = Cat("Luna")
zogu = Bird("Twiter")

for kafsha in (qeni,macja,zogu):
    kafsha.sound()