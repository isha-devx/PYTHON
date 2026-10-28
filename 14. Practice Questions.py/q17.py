# 17. print sum of all the numbers which are divisible by 2 and 7 from 1 to 100


start = int(input())
end = int(input())

i = start
total = 0
while i<=end:
    if i%2==0 and i%7==0:
        total = total + i
    i+=1
print(f"Total is {total}")

# 17. count all the numbers which are divisible by 2 and 7 from 1 to 100


start = int(input())
end = int(input())

i = start
count = 0
while i<=end:
    if i%2==0 and i%7==0:
        count = count + 1
    i+=1
print(f"Total is {count}")
