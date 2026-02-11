#Attached: HW_6a, 6b, 6c, 6d
# ===================================================
#Program: HW_6c (Item Counter)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will read the .txt file and print out
# the number of names that have been read
# ===================================================

with open('names.txt', 'r') as file:
    names = file.readlines()

num_names = len(names)

print(f"{num_names} names were read.")


# ===================================================
"""
OUTPUT
12 names were read.

"""
# ===================================================

