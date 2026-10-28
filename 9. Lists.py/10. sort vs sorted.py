nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 1, 1, 1]

#sort vs sorted
print(nums, id(nums))
new_list = sorted(nums) # this is not a method of list , this is a separate thing , it gives you a new list
print(new_list, id(new_list))

nums.sort()  #this sorts the list internally without creating a new list
print(nums, id(nums))