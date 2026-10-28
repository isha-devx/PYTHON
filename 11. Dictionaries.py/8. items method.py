marks = {
    "Science": 99, 
    "maths": 100, 
    "computer": 88,
    "hindi": 43,
    "history": 71,
}
#METHOD 1

#print(marks.items())          # returns all the items in the dictionary
#for detail in marks.items():
    #print(detail)
    #print(detail[0], detail[1])  # prints key and value of each item in the dictionary
    #sub = detail[0]
    #mark = detail[1]
    #print(sub, mark)  # prints key and value of each item in the dictionary

#METHOD 2

for sub, mark in marks.items():
    print(sub, mark)
