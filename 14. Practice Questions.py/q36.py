"""
write a function that print all the factors of a number entered by the userr.
"""
def factors():
    num=int(input("Enter a number: "))
    for i in range(1,num+1):
        if num%i==0:
            print(i, end=" ")
factors()
