student = {
    "name": "Rahul", 
    "age": 35,
    "gender" : "Male",
    "city" : "surat",
}
print(student ,id(student))

#REMOVE
#student.pop("name")
#print(student ,id(student))

#student.clear()
#print(student ,id(student))

del student["age"]
print(student ,id(student))