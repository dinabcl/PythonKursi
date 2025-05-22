def calculate(num1, num2, operatori):

    if operatori=="+":
        return num1+num2
    elif operatori=="-":
        return num1 - num2
    elif operatori=="*":
        return num1 * num2
    elif operatori=="/":
        return num1 / num2
    else:
       raise ValueError("Invalid operation")

try:
    nr1 = float(input("Enter a number"))
    nr2 = float(input("Enter a second number"))
    operatori=input("Enter an operation: + ,* ,- ,/")
    rezultati=calculate(nr1,nr2,operatori)
    print(f"The result of {nr1} {operatori} {nr2}:{rezultati}")
except ValueError as e:
    print(f"Invalid input {e}")
except ZeroDivisionError as e:
    print(f"Cannot divide by 0 input {e}")
except Exception as e:
    print(f"Error {e}")

finally:
    print("End of the program")