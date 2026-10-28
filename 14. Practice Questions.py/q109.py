"""
Q109
Take a string as input. Check if it is a valid Indian PAN card number.

Format: 5 uppercase letters + 4 digits + 1 uppercase letter
Total: 10 characters

"""
def validate_pan(pan:str):
    if len(pan) == 10 and pan[0:5].isupper() and pan[:5].isalpha() and pan[5:9].isdigit() and pan[9].isalpha():
        return True
    return False

pan = input("Enter PAN:")

print("Valid PAN" if validate_pan(pan) else "Invalid PAN")