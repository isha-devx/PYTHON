"""
Q108
Take a sentence as input. 
Capitalize only the first letter of each word longer than 3 characters.
keep the rest as it is.

"""
def capitalize_long_words(sentence:str):
    words = sentence.split()
    result = []
    for word in words:
        if len(word) > 3:
            word = word[0].upper() + word[1:]
        result.append(word)
    return " ".join(result)

sentence = "hello my friend python"
print(capitalize_long_words(sentence))
