"""
String Methods: Splitting and Joining
split(): Break String into List
join(): Combine List into String
"""
#SPLIT()
# text = "anirudh khurana is a coder"
# print(len(text.split("a")))

#JOIN()
#my_list = ["a", "n", "i", "r", "u", "d", "h"]
#print("".join(my_list))

#method 2
my_list = ["a", "n", "i", "r", "u", "d", "h", 5,55.33,"anirban"]
ans = "-".join(str(ch) for ch in my_list)
print((ans))
print(type(ans))

