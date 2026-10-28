marks = {
    "Science": 99, 
    "maths": 100, 
    "computer": 88,
    "hindi": 43,
    "history": 71,
    1: 10,
}
#print(marks["Science"])
#print(marks.get("Science", -1)) # -1 is default value if key is not found
#print(marks.get("Scieence", 0)) # 0 is default value if key is not found

subject = "hist"
ans = marks.get(subject)
if ans is None:
    print("Subject not found")
else:
    print(f"Marks in {subject} is {ans}")