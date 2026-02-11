#Attached: HW_3a, 3b, 3c, 3d
# ===================================================
#Program: HW_3b (Roman Numerals)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program asks the user for a number between 1-10
# and displays the corresponding roman numeral
# ===================================================

num = int(input("Enter a number between 1 - 10: "))
    
if 1 <= num <= 10:
    roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    roman_numeral = roman_numerals[num - 1]
    print(roman_numeral)
    
else:
    print("Error: Invalid Number")


# ===================================================
"""
OUTPUT
Enter a number between 1 - 10: 10
X

"""
# ===================================================
