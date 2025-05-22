#explicit TypeCasting kur hup vler shembull float to int cuz u lost the .02
age = 25
age_As_string=str(age)
print(age_As_string, " of type ", type(age_As_string))

print(bool(0)) #this is false because 0 is False in boolean
print(bool(1)) #this is true because 42 translates as 1

print(bool(""))
print(bool("Hello"))

#implicit TypeCasting
x=32
y=5.3
resultati=x+y
print(resultati, " of type ", type(resultati))

a=5
b="3"
resultati1= a*int(b)
print(resultati1, " of type ", type(resultati1))

c=4
resultati2="Hello"*c
print(resultati2, " of type", type(resultati2))

#get two numbers from user input and sum them up
num1=int(input("Enter a number: "))
num2=float(input("Enter a second numer: "))
print(num1 + num2)