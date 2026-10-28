#Strings are immutable

name = "Anirudh khurana"
print(name, id(name))
"""
print(name)
print(name[0])
print(name[2])
print(name[-1])
"""
#OVERWRITE
name = "isha"
print(name, id(name))
#name[0] = "z"      # you cannot assign like this it will give error
#print(name)     
name = 5
name = True
print(name, id(name))
