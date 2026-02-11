#Attached: HW_5a, 5b, 5c, 5d
# ===================================================
#Program: HW_5c (Maximum of Two Values)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user for two integers
# and return the greater value of the two
# ===================================================

def maximum(num1, num2):
    return max(num1, num2)

def main():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    max_num = maximum(num1, num2)
    print(f"The maximum number is: {max_num}")

if __name__ == "__main__":
    main()
    

# ===================================================
"""
OUTPUT
Enter number 1: 43
Enter number 2: 23
The maximum number is: 43

"""
# ===================================================