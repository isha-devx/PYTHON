#Q62
"""
Separate a list of integers into two distinct lines: one containing all the even numbers and the other containing all the odd numbers
"""

def separate_lstt(lst):
    odd_lst = []
    even_lst = []
    for num in lst:
        if num%2==0:
            even_lst.append(num)
        else:
            odd_lst.append(num)
    print(f"Even List = {even_lst}")
    print(f"Odd List = {odd_lst}")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
separate_lstt(nums)