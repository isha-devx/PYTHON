# simple for loop

fruits = {"apple", "kiwi" , "grapes", "mango", "litchi", "pomegranate"}
"""
for fruit in fruits:
    print(fruit)
"""
#looping through enumerate()

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")


