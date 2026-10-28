# write a function called find_max that takes three numbers as parameters and prints the largest one

def find_max(a,b,c):
    if a>b and a>c:
        print(f"{a} is greatest")
    elif b>a and b>c:
        print(f"{b} is greatest")
    else:
       print(f"{c} is greatest")
find_max(60,70,40)