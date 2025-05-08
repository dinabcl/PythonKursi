from PIL.ImageChops import difference

my_set={1,2,3,4,3,44}
print(my_set)
my_set_1=set([1,2,3,5,7,6])
print(my_set_1)

A={1,2,3}
B={3,4,5}

#find the union
unioni=A.union(B) #unioni = A | B
print(unioni)

#intersection
prerja=A.intersection(B) # prerja=A & B
print(prerja)

#difference
differenca=A.difference(B) #diferenca=A-B
print(differenca)

#diferenca simetrike
d_simetrike=A.symmetric_difference(B) #d_simetrike=A ni vi te nalt B
print(d_simetrike)

#add element
A.add(6)
print(A)

#remove element
A.remove(6)

#discard - remove an element without error if it does not exist
A.discard(100)

#removes all elementse
A.clear()

#find the number of elements  of a set
print(len(A))

list=[1,4,5,3,4]
C = set(list)
print(C)

set_1={"Elmedina","Dina","Dina", "Diana"}
set_2={"Elmedina","Melinda","Melisa", "Hana", "Rreze"}
prerja1=set_1.intersection(set_2)
print(prerja1)

#operatori In aedhe Not in
A=(1,2,3,4,5)
numri=1
print(numri in A) #true ose false nese numri eshte pjes e bashkesise
print(numri not in A)
