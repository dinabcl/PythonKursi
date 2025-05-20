total = 0

for number in range(1,11):
    if number%2==0:
        total+=number
print("The sum of the even number from 1 to 10 is ", total)

#this is the definishion of a function.Keyword def - in python defines functions. greet-emri i funksionit
def greet():
    print("Hello World!")
#this is how we use the function
greet()

def greet_person(name):
    print("Hello ",name)

greet_person("Alma")

def shuma(x,y): #this typw of function returns something in this case a number
    z=x+y
    return z

resultati= shuma(3,4)
print("3+4=", resultati )

#local variables - variablat e deklaurara lokalisht per brenda funskionit
def greet(name):
    message=f"Hello,{name}!"
    print(message)
greet("Alma")
#print(message) - this outputs an error because the message variable is defined only for the function

#argumentet dhe definimi i tyre
def greet_person(name, greeting="Hello"):
    message=f"{greeting}, {name}"
    return message
default_greeting=greet_person("Alma")
print(default_greeting)
custom_greeting=greet_person("Alma","Good Morning")
print(custom_greeting)

pershendetje="Hi"
def greet_people(name):
    global pershendetje
    return f"{pershendetje}, {name}"
variable=greet_people("Alma")
print(variable)

