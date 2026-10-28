student = {"name": "Rahul", "age": 21}
print(student, id(student))

#UPDATE
student["age"] = 30
print(student, id(student))

#ADD
student["gender"] = "Female"
#print(student, id(student))

student.update(
    {
        "city":"surat", 
        "phone": 876597054, 
        "state" : "Gujarat",
        "age" : 35,
    }
)
print(student, id(student))