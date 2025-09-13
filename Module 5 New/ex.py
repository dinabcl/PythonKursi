from email.policy import default

from pyexpat.errors import messages


def greet():
    print("Hello World!")

greet()

def greet_person(name):
    print("Hello, ", name)

greet_person("Eliza")

def gret(name):
    message = f"Hello, {name}!"
    print(message)

gret("Alexander")

#print(message) / error nuk e njeh variablen jasht funksionit

greeting = "Hi"

def greta(name):
    message = f"Hello, {name}!"
    print(message)

gret("Aron")

print(greeting)


greeting = "Hi"

def grata(name):
    global message
    message = f"Hello, {name}!"
    print(message)
grata("Angelica")
print(message)

message = f"{greeting}, Peggy"
print(message)

#me bo krejt comment perdoren """ ne fillim dhe fund te fjalis

greeting = "Hello"
name = "Ody"

def epic():
    global greeting
    greeting = "20 years"

    name = "Penelope"

    message = f"{greeting}, {name}"

    print(message)

epic()

print(greeting)
print(name)


def greet_person(name, greeting="Hello"):
    message = f"{greeting}, {name}"
    return message

default_greeting = greet_person("Alice")
custom_greeting = greet_person("Klee" , "Fire")

print(default_greeting)
print(custom_greeting)