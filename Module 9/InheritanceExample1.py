#class Superclass:

#class SubClass(Superclass): #ketu subklasa trashegon prej superklases

#__________________________________________________________

class Animal:
    def eat(self):
        print("This animal eats")
    def sleep(self):
        print("It sleeps")

class Bird(Animal):
    def fly(self):
        print("This animal flies in the sky")
    def sings(self):
        print("It sings")

bilbili = Bird()
bilbili.sings()
bilbili.fly()