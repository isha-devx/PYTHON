#Q55
#Calculate the Average

def calculate_average(nums):
    n = len(nums)
    total = 0
    for num in nums:
        total += num
    return total/n

nums = [6, -5, 4, 2, 10, 91, -75, 49, 9]
print(calculate_average(nums))