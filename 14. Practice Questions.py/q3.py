"""
3. take the users age as input. check and print whether they are eligible to vote (age>=18) and whether they are a senior citizen (age>+60). print both results.
"""

age = int(input("Enter Age:"))
print(f"User is eligible to vote: {age>=18}")
print(f"User is senior citizen: {age>=60}")