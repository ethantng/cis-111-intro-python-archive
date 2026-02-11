#Attached: HW_3a, 3b, 3c, 3d
# ===================================================
#Program: HW_3a (Days of the Week)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program asks the user for a number between 1-7
# and displays the corresponding day of the week
# ===================================================

num = int(input("Enter a number between 1 and 7: "))

if 1 <= num <= 7:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week = days[num - 1]
    print(f"The corresponding day of the week is {day_of_week}.")

else:
    print("Error: Please choose a number between (1-7).")


# ===================================================
"""
OUTPUT
Enter a number between 1 and 7: 3
The corresponding day of the week is Wednesday.

"""
# ===================================================
