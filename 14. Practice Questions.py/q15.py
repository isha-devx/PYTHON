# print al the numbers which are divisible by 3 and 5, from 1 to 100

a = 1
b = 100

i = a 
while i<=b:
    if i%3==0 and i%5==0:
        print(i, end=" ")
    i+=1

