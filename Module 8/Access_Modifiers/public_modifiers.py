class MyClass:

    def __init__(self):
        self.public_variable = "This is a public varibale"

    def public_method(self):
        print("This is a public method")
#me kriju nje varible ose metod publike nuk ja shtojna ne fillim asgje
my_class = MyClass()

print(my_class.public_variable)
my_class.public_method()