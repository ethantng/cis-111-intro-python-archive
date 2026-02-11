#Attached: HW_9a, 9b, 9c, 9d
# ===================================================
#Program: HW_9b (Word Separator)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user to input a string
# then displays the string with separate words
# ===================================================

def sep(sentence):
    words = []
    input_word = ""
    for char in sentence:
        if char.isupper():
            if input_word:
                words.append(input_word)
            input_word = char.lower()
        else:
            input_word += char
    if input_word:
        words.append(input_word)
    return " ".join(words)

user_input = input("Enter a string: ")

result = sep(user_input)
print(result)


# ===================================================
"""
OUTPUT
Enter a string: MyNameIsEthanNguyenAndIAmTakingPython
my name is ethan nguyen and i am taking python

"""
# ===================================================

