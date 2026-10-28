"""
take numbers as input from the user one by one. skip negative numbers and keep adding the positive ones. stop when the user enters 0 and print the total. (uses both continue and break)
"""
total = 0
while True:
    num = int(input("Enter a number:"))
    if num==0:
        break
    if num<0:
        continue
    total+=1
print(total)
    