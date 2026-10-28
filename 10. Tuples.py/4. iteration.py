my_tuple = (45, 32, 11, "Isha", "Ranchi", "Lohani")

n = len(my_tuple)
for i in range(0,n):
    print(my_tuple[i],end=" ")
print()

for ele in my_tuple:
    print(ele,end=" ")
print()

for index,value in enumerate(my_tuple):
    print(f"Index = {index} and Value = {value}")
print()