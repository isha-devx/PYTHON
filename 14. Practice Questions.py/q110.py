"""
Q110.
Write a function that returns the word occurring most frequently in a paragraph.
Ignore case. If multiple words have the same count, return any one.
"""
def most_common_word(text: str):
    words = text.lower().split()

    count = {}

    most_common = ""
    highest = 0

    for word in count:
        if count[word] > highest:
            highest = count[word]
            most_common = word

    return most_common


sentence = input("Enter a sentence: ")
print(most_common_word(sentence))



shampoo - scalppro
serum and conditioner - lorreal