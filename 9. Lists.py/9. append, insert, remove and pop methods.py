#APPEND
lst = ["Isha", 54, 21.98, True, "Surat"]
#print(lst)
lst.append(100)
lst.append("Ishaaaaaaaa")
#print(lst)

#INSERT
lst = ["Isha", 54, 21.98, True, "Surat"]
#print(lst)
lst.insert(2, "ishaaaaa")
#print(lst)

#REMOVE
lst = ["Isha", 54, 21.98, True, "Surat"]
print(lst)
lst.remove((54))
print(lst)

#POP
lst = ["Isha", 54, 21.98, True, "Surat"]
#print(lst)

#x = lst.pop()
#print(x)
#print(lst)

lst = ["Isha", 21, 21.98, True, "Delhi"]
print(lst, id(lst))
#LIST METHODS 
lst.append("Amisha")
print(lst)
lst.insert(2, "DSLR")
print(lst)
lst.pop(1) #by index
print(lst)
lst.remove(True)   #by value
print(lst, id(lst))