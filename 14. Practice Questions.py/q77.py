#Q77
#Take 5 numbers as input from the user, store them in a tuple, and print the tuple along with its minimum and maximum.

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
num4 = int(input("Enter fourth number:"))
num5 = int(input("Enter fifth number:"))

numbers = (num1, num2, num3, num4, num5)
print(numbers)
print(f"{min(numbers)} is Minimum number")
print(f"{max(numbers)} is Maximum number")