try:
    result=10/0
except ZeroDivisionError:
    print("Error, cant devide numbers with zero")

#example 2

text = "This is not a number"

try:
    text_to_int= int(text)
except Exception as e:
    print("An error occured :", e)

#example 3

try:
    result=10/2
except ZeroDivisionError:
    print("Error, cant devide numbers with zero")
else:
    print("Division succsesful. Result: ", result)