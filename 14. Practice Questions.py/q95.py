"""
Q95.
Read a sentence from the user. Count and print the total number of vowels (a,e,i,o,u, case-insensitive) present in it, using a for loop.
"""

sent = "I will land GOOGLE one day"

n = len(sent)
total = 0

for ch in sent:
    if ch in "aeiouAEIOU":
        total +=1
print(total)