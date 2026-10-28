#Q79
#Create a dict for a student, including keys like name, age, city and marks(as a list of scores). print each piece of information using its keys

students = {
    "name": "Isha",
    "age": 20,
    "city": "New York",
    "marks": [78, 85, 92],
}

for key in students:
    print(key, ":", students[key])