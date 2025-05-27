class MyClass:
    def __init__(self):
        self.__private_variable = "This is a private variable"

    def __private_method(self):
        print("This is a privet method")
#me kriju nje varible ose metod private ja shtojna ne fillim __
my_class = MyClass()

print(my_class.__private_variable)

print(my_class.__private_method())
