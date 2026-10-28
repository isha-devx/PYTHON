"""
students = {
    "101": {"name": "Rahul", "age": 21, "city": "Delhi"},
    "102": {"name": "Priya", "age": 20, "city": "Mumbai"},
    "103": {
        "name": "Karan", 
        "age": 22, 
        "city": "Pune",
        "details": {"ph": 81881, "gender": "Male"}
        },
}

#HOW TO ACCESS
#print(students["101"])
#print(students["102"]["age"])
#print(students["103"]["name"])
#print(students["103"]["details"]["ph"])
#print(students["103"]["details"]["gender"])
"""

#FOR LOOP
students = {
    "101": {"name": "Rahul", "age": 21, "city": "Delhi"},
    "102": {"name": "Priya", "age": 20, "city": "Mumbai"},
    "103": {"name": "Karan", "age": 22, "city": "Pune"},
}
total = 0
for roll_no, details in students.items():
    total += details["age"]
    print(f"roll_no = {roll_no}, name = {details['name']}, age = {details["age"]}, city = {details["city"]} ")
print(total)