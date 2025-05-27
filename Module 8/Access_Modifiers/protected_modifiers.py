class MyClass:

    def __init__(self):
        self._protected_variable = "This is a protected varibale"

    def _protected_method(self):
        print("This is a protected method")
#me kriju nje varible ose metod private ja shtojna ne fillim _
my_class = MyClass()

print(my_class._protected_variable)
my_class._protected_method()