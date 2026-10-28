#local variable

def xyz(n1,n2):
    n1=100   # local variable
    n2=200   # local variable
    print(f"Inside function n1= {n1} and n2={n2}")

a=10    # global variable
b=20    # global variable
xyz(a,b)
print(a)
print(b)
