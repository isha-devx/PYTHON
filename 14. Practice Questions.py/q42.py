# write a function called min_of_three that takes three numbers an dreturns the smallest without using any built-in function

def min_of_three(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c
ans= min_of_three(10,67,3)
print(f"smallest is {ans}")