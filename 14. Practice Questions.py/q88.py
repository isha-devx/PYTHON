#Q88
#Design a dictionary where each key is a student's name and the corresponding value is a list of thier marks in 3 different subjects. Calculate and print total marks and average marks for each student.

students = {
    "Alice": [85, 92, 78],
    "Bob": [70, 65, 80, 11],
    "Charlie": [90, 88, 95, 11, 76],
    "Diana": [60, 74, 68],
    "Ethan": [55, 48, 62],
}

for name, marks in students.items():
    total = sum(marks)
    avg = total/len(marks)
    print(f"{name} has scored total of {total} and avg of {avg:.2f}")
    
