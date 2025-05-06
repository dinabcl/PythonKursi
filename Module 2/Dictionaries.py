#collection of items, mutable, not indexable, works on a pair key: value
contact_info={
    "Alma":"049123456",
    "Erin":"049654321"
}
print(contact_info)
alma_info=contact_info["Alma"]
print(alma_info)
contact_info["Orkidea"]="049000123"
contact_info["orkidea"]="049000123"
del contact_info["orkidea"] #me fshi ni element
print(contact_info)
keys=contact_info.keys()#me i printu veq keyes
print(keys)
values=contact_info.values()#me i printu veq values
print(values)
items=contact_info.items()
print(items) #print out the key-value pair as lists
