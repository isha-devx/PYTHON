#Q87
#Create a nested dictionary containing details for 4 students, here each student entry includes thier name, age, and city. write a loop to print the full details of each student in a clear, readable format.

students = {
    "student1": {
        "name": "Kartik",
        "age": 20,
        "city": "Ranchi"
    },
    "student2": {
        "name": "Tanmay",
        "age": 21,
        "city": "Delhi"
    },
    "student3": {
        "name": "Gautam",
        "age": 19,
        "city": "Patna"
    },
    "student4": {
        "name": "Pratik",
        "age": 20,
        "city": "Bangalore"
    }
}

for students, details in students.items():
    print(students)
    print("name:", details["name"])
    print("Age:", details["age"])
    print("City:", details["city"])
    print()