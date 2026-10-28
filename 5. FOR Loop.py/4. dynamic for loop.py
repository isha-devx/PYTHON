#start and end print

start=int(input("enter start"))
end=int(input("enter end"))
total = 0

for i in range(start, end+1):
    total = total + i 
print(f"total is {total}")