contact_info={
    "Alice":{
        "Phone":"049444444",
        "email":"alice@gmail.com",
        "address":"123 rruga kryesose Prishtine",
        "birthday":"20/11/1997"
    },
    "Bob":{
        "Phone":"049444444",
        "email":"bob@gmail.com",
        "address":"123 rruga dytesore Prishtine",
        "birthday":"20/08/1997"
    },
    "Eve": {
        "Phone": "049444444",
        "email": "eve@gmail.com",
        "address": "123 rruga kryesose Prishtine",
        "birthday": "17/11/1997"
    }
}

print(contact_info)
#1. print out Bob's info
print(contact_info["Bob"])
#2. create two new personas jANE AND JHON
contact_info["Jane"]={
    "Phone": "049444444",
    "email": "jane@gmail.com",
    "address": "123 rruga kryesose Prishtine",
    "birthday": "17/11/1997"
}

contact_info["John"]={
    "Phone": "049444444",
    "email": "john@gmail.com",
    "address": "123 rruga kryesose Prishtine",
    "birthday": "17/11/1997"
}

#3 PRINT JANES INFO
print(contact_info["Jane"])
#4 UPDATE JANES PHONE NUMER AND PRINT
contact_info["Jane"]["Phone"]="049111111"
print(contact_info["Jane"]["Phone"])
