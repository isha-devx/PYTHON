#Q84
#Populate a dict with six student names and thier corresponding scores. iterate through it and print the names of all the students who achieved a score above 75

students = {
    "kartik": 89,
    "tanmay": 67,
    "gautam": 87,
    "pratik": 56,
    "swastik": 78,
    "abhay": 64,
}

for name, score in students.items():
    if score>75:
        print(name)
    