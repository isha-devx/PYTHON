#Q78
#Write a function get_stats(nums) that takes a tuple of numbers and returns a tuple containing the sum, average, minimum. Unpack the returned tuple and print each value.

def get_stats(nums):
    total = sum(nums)
    average = total / len(nums)
    mini = min(nums)
    return total, average, mini


total, average, mini = get_stats((1, 2, 5, 7, 9, 10))

print(f"Total = {total}")
print(f"Average = {average}")
print(f"Minimum = {mini}")