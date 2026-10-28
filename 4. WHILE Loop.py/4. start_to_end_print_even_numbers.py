#start to end print even numbers 


start = int(input())
end = int(input())

i = start 
while i<=end:
    if i%2==0:
        print(i, end = " ")
    i+=1
print(f"After while loop start value is {start}")
