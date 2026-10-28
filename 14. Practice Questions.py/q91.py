#Q91
#Given an existing dictionary of subjects and thier respective marks, use dictionary comprehension to generate a new dictionary the     only the subjects where the student scored 40 or more(passed).

subjects = {
    "Python": 85,
    "Java": 35,
    "Maths": 72,
    "English": 40,
    "SQL": 28,
    "Computer": 65
}

passed = {subject: marks for subject, marks in subjects.items() if marks >= 40}
print(passed)
