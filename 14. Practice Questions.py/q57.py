#Q57
#Check if a list is sorted
"""
#1
number = [1, 5, 10, 15, 20]
expected output: True
#2
number = [1, 10, 5, 15, 20]
expected output: False
#3
number = []
expected output: True(an empty list is considered sorted)
"""

def is_sorted(lst):
    n=len(lst)
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True   
        
nums = [3, 6, 8, 13, 9, 17, 18, 23, 45, 58, 79, 100]
a = is_sorted(nums)
print(a)