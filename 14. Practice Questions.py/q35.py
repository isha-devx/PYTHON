"""
write a function that ask a number from the user and prints if that number is odd or even.
"""

def odd_even():
    num=int(input("Enter Number:"))
    if num%2==0:
        print(f"{num} is Even")
    else:
        print(f"{num} is odd.")
odd_even()