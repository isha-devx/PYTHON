marks = {
    "Science": 99, 
    "maths": 100, 
    "computer": 88,
    "hindi": 43,
    "history": 71,
}
total = 0
#print(marks.keys())          # returns all the keys in the dictionary
for sub in marks.keys():
    #print(sub, marks[sub])  # prints key and value of each item in the dictionary
    print(f"Subject = {sub} and Marks = {marks[sub]}")
    total = total + marks[sub]
print(f"Total Marks = {total}")  

#METHOD 2
for k in marks:
    print(k)