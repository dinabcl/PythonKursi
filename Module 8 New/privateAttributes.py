class MyClass:
    def __init__(self):
        self.__private_var = "This is a private variable"
    def __private_method(self):
        print("This is a private method")

myClass = MyClass()

#Attributes Error
print(myClass.__private_var)
myClass.__private_method()