#Q.58
"""
Find the smallest number without using min() function.
"""

nums = [155, 29, 311, 45, 78,]

mini = 100
n = len(nums)
for i in nums:
    if i<mini:
        mini = i
print(mini)
    


