#per elementin ne sekuencen
names=["Alma","Blerta","Dhurata","Shpati"]
for name in names:
    print(name)


#shembulli 2
sentence_shembulli="Hello World"
for char in sentence_shembulli:
    if char.isalpha(): #kthen true or false if char is a letter
        print(char)


#shembulli 3 me range function
for numri in range(1,6):#range(x,y) x-fillon y-ku mbaron nuk perfshihet y
    print(numri)

#shembulli 4 find max ne nje list
numat=[33,44,45,55,23,12,94,100,101]
max=numat[0]
for num in numat:
    if num>max:
        max=num
print("The maximum value of the list is ", max)

