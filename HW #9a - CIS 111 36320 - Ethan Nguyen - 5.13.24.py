#Attached: HW_9a, 9b, 9c, 9d
# ===================================================
#Program: HW_9a (Most Frequent Character)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user to input a string
# then displays the character that appears most frequently
# ===================================================

def freq_char(s):
    count = {}
    for char in s:
        if char.isalpha():
            char = char.upper()
            count[char] = count.get(char, 0) + 1
    
    freq_char1 = max(count, key = count.get)
    return freq_char1

user_input = input("Enter a string: ")
    
freq_char1 = freq_char(user_input)

print(f"The string that appears the most frequently in the string is {freq_char1}")


# ===================================================
"""
OUTPUT
Enter a string: Ethan Nguyen
The string that appears the most frequently in the string is N

"""
# ===================================================

