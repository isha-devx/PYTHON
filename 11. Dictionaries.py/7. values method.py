marks = {
    "Science": 99, 
    "maths": 100, 
    "computer": 88,
    "hindi": 43,
    "history": 71,
    1: 10,
}
total = 0
#print(marks.values())         # returns all the values in the dictionary
for mark in marks.values():
    print(mark)      
    total = total + mark
print(f"Total Marks = {total}")  # prints value of each item in the dictionary