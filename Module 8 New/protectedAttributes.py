class MyClass:
    def __init__(self):
        self._protected_var = "This is a private variable"
    def _protected_method(self):
        print("This is a private method")

myClass = MyClass()

print(myClass._protected_var)
myClass._protected_method()