"""
10. take a year as input. check if it is a leap year. a year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.
"""

Year = int(input("Enter Year:"))

if (Year%4==0) and (Year%100!=0) or (Year%400==0):
    print(f"{Year} is a Leap Year")
else:
    print("Year is not Leap Year")