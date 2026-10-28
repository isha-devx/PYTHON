#
subjects = ["Python", "Java", "Maths", "SQL"]
marks = [85, 72, 90, 78]

result = {subject: mark for subject, mark in zip(subjects, marks)}

print(result)
