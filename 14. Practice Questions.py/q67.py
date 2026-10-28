#67
"""
Given a list of marks, use list comprehension to create a new list that contains only the marks that are above 75.
"""
list = [ 12,68,78,98,4,5,6,987]
new_list = [i for i in list if i>75]
print(new_list)