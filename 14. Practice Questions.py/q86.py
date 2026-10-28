#Q86
#Create a dictionary of 6 subjects and thier respective marks. Print the subject with the highest marks and the one with the lowest, using max() and min() functions alongside a lambda expression.

subjects = {
    "maths": 66,
    "science": 78,
    "history": 98,
    "hindi": 67,
    "physics": 56,
    "chemistry": 48,
}

maxi = max(subjects, key=lambda x: subjects[x])
mini = min(subjects, key=lambda x: subjects[x])

print(maxi)
print(mini)