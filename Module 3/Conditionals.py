#kushetet dhe kontrolla e flow-it te programit
# == nese jan te barabatra dy variabla
# != nese nuk jan te barabrata
# < me e vogel se
# > me e madhe se
# <= dhe >= barazi ose ma e madhe/ vogel se
# operatoret logjik
# and or not

#indentation 4 spaces ose 1 tab

#shembulli 1:
age = int(input("Sa vjec jeni?"))
if age >= 15:
    print("Je i pranuar ne shkollen digjitale adv level")
else:
    print("Code.org")

#shembulli 2:

temperatura=28
if temperatura > 30:
    print("Its hot a hot, stay inside")
elif 20<=temperatura<=30: #new comand for else if
    print("The weather is nice!")
else:
    print("Its cold")
