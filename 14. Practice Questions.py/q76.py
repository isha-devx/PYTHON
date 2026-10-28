#Q76
#Create a tuple of marks of 6 students. Print the highest, lowest, total and average.

marks = (45,75,77,89,90,99)
print(f"Highest Marks = {max(marks)}")
print(f"Lowest Marks = {min(marks)}")
total = sum(marks)
print(f"Total Marks = {total}")
average = total/len(marks)
print(f"Average Marks = {average}")