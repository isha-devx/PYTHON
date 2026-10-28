"""
8. take two numbers as input. print the greater of the two, if they are equal, print "both are equal".
"""

num1 = int(input("Enter Number 1:"))
num2 = int(input("Enter Number 2:"))

if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num2>num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both are equal")