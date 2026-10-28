#Q54
#Check for Target Existence
"""
my_list = [10, 20, 30, 40, 50]
target = 30
expected output: 30 exists in the list

target = 60
expected output: 60 does not exist in the list.
"""
def does_target_exist(lst,target):
    for num in lst:
        if num==target:
            return True
    return False

nums = [6, -5, 4, 2, 10, 91, -75, 49, 9]

print(does_target_exist(nums, 49))