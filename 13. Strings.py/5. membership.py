
text = "Programming"
"""
in / not in

print("p" in text)
print("p" in text)
print("z" not in text)
print("z" in text)
print("gram" in text)
 
# question 2
n = len(text)
total = 0
for i in range(0,n):
    if text[i] == "a" or text[i] == "e" or text[i] == "i" or text[i] == "o" or text[i] == "u":
        total = +1
print(total)
"""
total = 0
for ch in text:
    if ch in "aeiouAEIOU":
        total +=1
print(total)



