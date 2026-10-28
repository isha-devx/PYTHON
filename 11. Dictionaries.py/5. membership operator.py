student = {
    "name": "Rahul", 
    "age": 35,
    "gender" : "Male",
    "city" : "surat",
}

#print("age" in student) #TRUE because "age" is a key in the dictionary
#print(35 in student) #FALSE because 35 is not a key in the dictionary, it is a value

K = input("Enter key:")

if K in student:
    print(student[K])
else:
    print("key does not exist")
