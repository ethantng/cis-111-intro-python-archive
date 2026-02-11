#Attached: HW_6a, 6b, 6c, 6d
# ===================================================
#Program: HW_6d (Sum of Numbers)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will read the .txt file and print out
# the sum of the numbers within the file
# ===================================================

with open('numbers.txt', 'r') as file:
    numbers = file.readlines()

total = 0

for number in numbers:
    total += int(number)

print(f"Total: {total}")


# ===================================================
"""
OUTPUT
Total: 99

"""
# ===================================================