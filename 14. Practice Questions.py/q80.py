#Q80
#Define a dict with five subjects and their respective marks. Utilize the get() method to try accessing a subject that is not in the dictionaryu, ensuring it prints "Not Available" as a default.

subjects = {
    "Maths": 56,
    "English": 90,
    "Physics": 78,
    "Chemistry": 67,
    "Computer": 88,
}

sub = "Biology"
ans = subjects.get(sub)
if ans is not None:
    print(f"Marks in {sub} is {ans}")
else:
    print("Not Available")
