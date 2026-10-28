#age>=18
#certificate=true
#then only you are hired

age = int(input("Enter Age:"))
certificate = input("Do you have certificate?")

if(age>=18):
    if (certificate=="yes"):
        print("You are Hired")
    else:
        print("You are not Hired")
else:
    print("You are too young to be hired")