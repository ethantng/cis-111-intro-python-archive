#Attached: HW_6a, 6b, 6c, 6d
# ===================================================
#Program: HW_6a (File Display)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will read the file 'name.txt' and 
# display whatever is on the file
# ===================================================

with open('name.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())


# ===================================================
"""
OUTPUT
I attend Santiago Canyon College.
I am taking CIS_111.

"""
# ===================================================

