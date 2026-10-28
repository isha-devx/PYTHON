#Q59
"""
Reverse a list without using a reverse() method or list slicing[::-1].
"""
#       0  1  2  3  4  5  6  7  8  9  10 11
nums = [1, 7, 8, 5, 6, 4, 0, 2, 8, 9, 4, 3]
#     -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1  0

n = len(nums)
new_list = []
for i in range(n-1,-1,-1):
    new_list.append(nums[i])
    i+=1
print(new_list)