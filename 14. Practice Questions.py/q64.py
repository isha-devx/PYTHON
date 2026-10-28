#Q64
"""
Given a list of numbers (which may contain duplicates), write a python script that takes an integer as input from the user and removes all occurrences of that integer from the list 
"""
#method 1
"""
def numbers(lst,target):
    new_lst =[]
    for num in lst:
        if num!=target:
            new_lst.append(num)
    return(new_lst)

nums =[1, 2, 2, 3, 6, 8, 9, 4, 5, 0]
print(numbers(nums,2))
"""
#method2
def numbers(lst,target):
    while target in lst:
        lst.remove(target)
    return lst


nums =[1, 2, 2, 3, 6, 8, 9, 4, 5, 0]
print(numbers(nums, 2))

