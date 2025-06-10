#decorators getters and setters
class Student:
    def __init__(self,name,age): #konstruktori i klases e cila eshte pjesa qe behet run e para
        self.__name=name #ketu deklatorhen te gjihta atributetet e klases
        self.__age=age
    # deklarimi i metodes get
    @property
    def name(self):
        return self.__name

    #deklarimi i metodes set
    @name.settter
    def name(self, name):
        self.__name=name

    # deklarimi i metodes get
    @property
    def age(self):
        return self.__age

    #deklarimi i metodes set
    @age.settter
    def age(self, age):
        self.__age=age

student1=Student("Elmedina",17)

print("Name", student1.name)

student1.name="Bob"
student1.age=18

print("Name:", student1.name)