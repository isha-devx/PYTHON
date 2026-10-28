nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]

#print(100 in nums)
#print(1 in nums)

#question
target = int(input("Enter Target:"))
if target in nums:
    nums.remove(target)
    print(nums)
else:
    print("target doesn't exist")