lines=["Hello World!\n","Welcome to Python\n"] #these write on the other file
with open("example.txt","w") as file:#we open the file with premission to write
    file.writelines(lines) #we write on multiple lines
