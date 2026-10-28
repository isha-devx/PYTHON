#Q65
"""
Write a python script that iterates through a list of integers and replaces every negative number found in the list with the value 0.
"""
def replace_negative(lst):
    n = len(lst)
    for i in range(0,n):
        if lst[i]<0:
            lst[i]=0
    return lst
    
nums = [1, -2, 3, 0, -5, -6, 8]
result = replace_negative(nums)
print(result)