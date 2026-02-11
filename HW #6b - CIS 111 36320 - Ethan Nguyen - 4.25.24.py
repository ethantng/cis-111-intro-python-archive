#Attached: HW_6a, 6b, 6c, 6d
# ===================================================
#Program: HW_6b (File Display)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user to input the file
# name and display the first 5 lines
# ===================================================

file_name = input("Enter the name of the file: ")

try:
    with open('test.txt', 'r') as file:
        lines = file.readlines()[:5]

        for line in lines:
            print(line.strip())
            
except FileNotFoundError:
    print("File not found.")


# ===================================================
"""
OUTPUT
Enter the name of the file: test.txt
one
two
three
four
five

"""
# ===================================================

