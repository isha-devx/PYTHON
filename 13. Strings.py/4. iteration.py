#text = "Programming"
"""
FOR LOOP
#method 1

n = len(text)
total = 0
for i in range(0,n):
    if text[i] =="o" or text[i] == "O":
        total+=1
print(total)

#method 2

for ch in text:
    print(ch)
"""
"""
#WHILE LOOP

n = len(text)
total = 0
i = 0
while i < n:
    if text[i] == "m" or text[i] == "M":
        total+=1
    i+=1
print(total)
"""

#ENUMERATE

text = "Programming"

for ind, ch in enumerate(text):
    print(f"ind = {ind} and ch = {ch}")