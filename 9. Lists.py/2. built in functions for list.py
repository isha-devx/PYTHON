marks = [45,34,54,65,23,65,76,91]

n = len(marks)
print(f"Length = {n}")

maxi = max(marks)
print(f"Maximum = {maxi}")

mini = min(marks)
print(f"Minimum = {mini}")

add = sum(marks)
print(f"Sum = {add}")

# To sort using sorted(), it will always return you a new list 
new_list = sorted(marks)
new_list_reverse = sorted(marks, reverse=True)
print(f"New list ={new_list}")
print(f"Marks = {marks}")
print(f"Reversed list = {new_list_reverse}")


"""
# Mixing the list 
marks = [45,34,54,65,23,65,76,91, "isha"]

n = len(marks)
print(f"Length = {n}")

maxi = max(marks)
print(f"Maximum = {maxi}")

mini = min(marks)
print(f"Minimum = {mini}")

add = sum(marks)
print(f"Sum = {add}")

# this code will give error
"""
