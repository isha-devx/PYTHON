#Q53
#Find the largest element without max() function.
"""
nums = [6, -5, 4, 2, 10, 91, -75, 49, 9]

maxi = 0
n = len(nums)
for i in nums:
    if i>maxi:
        maxi = i

print(maxi)
"""

nums = [-6, -5, -4, -2, -10, -91, -75, -49, -9]

maxi = float("-inf")
n = len(nums)
for i in nums:
    if i>maxi:
        maxi = i

print(maxi)

