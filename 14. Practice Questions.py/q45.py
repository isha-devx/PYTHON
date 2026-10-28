"""
Q45
write a lambda function that takes a number and returns "Positive", or "Negative".
"""

is_positive = lambda num: "Positive" if num>=0 else "Negative"

print(is_positive(5))
print(is_positive(-99))