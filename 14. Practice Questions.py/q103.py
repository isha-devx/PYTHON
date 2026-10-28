"""
Q103. Username Validation

Take a username as input. Strip any spaces from both sides and check if the
cleaned name starts with a letter (not a digit). Print "Valid" or "Invalid".
"""
def clean_username(username:str):
    words = username.strip()
    if words[0].isdigit():
        return "Invalid"
    return "Valid"

username = "  1Anirudh123"
print(clean_username(username))