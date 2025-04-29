name_of_list=["item1","item2","item3","item4","item5"]
shopping_list=["banane",3.2,3]
colors_list=["Blue","Pink","Red","Orange","Yellow"]
colors_list.append("Purple") #shton element te ri ne fund te listes
#colors_list.clear() #fshin krejt elementet e listes
#colors_list.count() #i numreron elementet
colors2 = colors_list.copy() #e kopjon listen
colors2.insert(1,"item10")#adds the element to the specific place
print("lista 2", colors2)
colors2.pop(1)# removes from specific place
colors2.remove("Pink") #removes based on value
colors2.reverse() #reverses the elements
print(colors2[-1])#acessing the last element of the list 
print(colors2)
print(colors_list)

