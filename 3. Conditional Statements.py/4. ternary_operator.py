#normal way
"""
age = int(input("Enter Age:"))

if (age>=18):
    status = "Adult"
else:
    status = "Minor"
print(f"Your status is {status}")
"""

#shorthand way

age = int(input("Enter Age:"))
status = "Adult" if age>=18 else "Minor"
print(f"Your status is {status}")