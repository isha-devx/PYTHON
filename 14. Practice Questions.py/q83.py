#Q83
#Given a dict of marks for different subjects, loop over its values() to calculate and print the total marks and the average mark obtained.

subjects = {
    "english": 88,
    "hindi": 99,
    "maths": 90,
    "science": 78,
}
total = 0
average = 0
for mark in subjects.values():
    total+= mark
    average = total/len(subjects)
print(total)
print(average)
