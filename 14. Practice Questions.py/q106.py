"""
Q106. Word Lengths (Homework)

Take a sentence as input. Print each word's length next to it.
Example: Python (6) is (2) great (5).
"""
def count_words_length(sentence:str):
    words = sentence.split()
    result = []
    for word in words:
        result.append(word + " (" + str(len(word)) + ")" )
    return " ".join(result)

sentence = "Anirudh is learning Python programming every single day"
print(count_words_length(sentence))
