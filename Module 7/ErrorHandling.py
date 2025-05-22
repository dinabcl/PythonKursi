#Error Handling Try, Except, Finally
#Try - writing of the needed code
#Except - what happens if an error happens in the try part
#Finally - Part of code that is always run

#This is dedicated for errors that programmers do not predict
#Shembulli 1
try:
    print("Pjesto dy numra")
    nr1 =int(input("Shkruani nr1"))
    nr2 =int(input("Shkruani nr2"))
    resultati = nr1/nr2
    print(resultati)
except ZeroDivisionError:
    print("Ke gabu per shkak qe e je duke pjestuar me zero")

#Shembulli 2
#Dictionaries
fruits={
    "Apples":5,
    "Bananas":6,
    "Oranges":7
}

try:
    print(fruits["Bananas"])
except KeyError:
    print("The key does not exist in the dictionary")


#Shembulli 3
text = "This is not a number"
try:
    text_to_int=int(text)
except Exception as e:
    print("An error occurred while parsing the data: ", e)


#Shembulli 4
try:
    resultati=10/2
except ZeroDivisionError:
    print("Division by zero error occurred ")
else:
    print("Division successful, Result: ", resultati)


#Shembulli 5
try:
    resultati=10/0
except ZeroDivisionError:
    print("Division by zero error occurred ")
finally:
    print("This part of code always runs")