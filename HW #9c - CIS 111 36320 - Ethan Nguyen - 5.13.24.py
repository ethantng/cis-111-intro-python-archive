#Attached: HW_9a, 9b, 9c, 9d
# ===================================================
#Program: HW_9c (Sentence Capitalizer)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user to input a string
# then capitalize the beginning of each sentence
# ===================================================

def capitalize(s):
    result = ""
    cap = True
    for char in s:
        if cap and char.isalpha():
            result += char.upper()
            cap = False
        else:
            result += char
        if char in [".", "!", "?"]:
            cap = True
    return result

user_input = input("Enter a string for the program to capitalize sentences: ")

result = capitalize(user_input)
print(result)


# ===================================================
"""
OUTPUT
Enter a string for the program to capitalize sentences: my name is ethan. i am 19 years old.
My name is ethan. I am 19 years old.

"""
# ===================================================

