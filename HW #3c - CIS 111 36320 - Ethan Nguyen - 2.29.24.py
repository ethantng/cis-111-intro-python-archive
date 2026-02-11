#Attached: HW_3a, 3b, 3c, 3d
# ===================================================
#Program: HW_3c (Magic Dates)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program asks the user for a date and determines
# whether the month tiems the day equals the year
# ===================================================

month = int(input("Enter the month in numeric form: "))
day = int(input("Enter the day of the month: "))
year = int(input("Enter the year in a two-digit format: "))
print(f"The date is {month}/{day}/{year}")

magic = month * day

if magic == year:
    print("This is a magic date.")
else:
    print("This is not a magic date.")
    

# ===================================================
"""
OUTPUT
Enter the month in numeric form: 6
Enter the day of the month: 3 
Enter the year in a two-digit format: 18
The date is 6/3/18
This is a magic date.

"""
# ===================================================
