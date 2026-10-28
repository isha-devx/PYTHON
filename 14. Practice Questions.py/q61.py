#61
"""
Given a list, remove all duplicate elements while preserving the original order of the unique items.
"""
def remove_duplicates(lst):
    result =[]
    for num in lst:
        if num not in result:
            result.append(num)
    return result

nums = [1, 7, 7, 6, 5, 5, 1, 1, 7, 8, 9, 10, 10]
print(remove_duplicates(nums))
