GPA = float(input("What is your GPA?"))
testScore = int(input("What is your test score?"))
if GPA >=3.5 and testScore >= 65:
    print("You won a full scholarship")
elif GPA >=3.5 and testScore >= 50:
    print("You won a partial scholarship")
elif GPA >= 3.5 and testScore <= 50:
    print("You didnt win a scholarship")
else:
    print("You didnt win a schoolarship")
