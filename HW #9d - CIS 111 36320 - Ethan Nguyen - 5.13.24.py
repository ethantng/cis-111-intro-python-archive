#Attached: HW_9a, 9b, 9c, 9d
# ===================================================
#Program: HW_9d (Alphabetic Telephone Number Translator)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user to input a phone number
# then the program should display the number with
# its alphabetic character equivalent
# ===================================================

def numeric_translator(phone_number):
    numeric = ""
    for char in phone_number:
        if char.isalpha():
            if char.upper() in "ABC":
                numeric += "2"
            elif char.upper() in "DEF":
                numeric += "3"
            elif char.upper() in "GHI":
                numeric += "4"
            elif char.upper() in "JKL":
                numeric += "5"
            elif char.upper() in "MNO":
                numeric += "6"
            elif char.upper() in "PQRS":
                numeric += "7"
            elif char.upper() in "TUV":
                numeric += "8"
            elif char.upper() in "WXYZ":
                numeric += "9"
        else:
            numeric += char
    return numeric

user_input = input("Enter the telephone number in the format XXX-XXX-XXXX: ")

numeric = numeric_translator(user_input)
print("The phone number is", numeric)


# ===================================================
"""
OUTPUT
Enter the telephone number in the format XXX-XXX-XXXX: 555-EAT-FOOD
The phone number is 555-328-3663

"""
# ===================================================


