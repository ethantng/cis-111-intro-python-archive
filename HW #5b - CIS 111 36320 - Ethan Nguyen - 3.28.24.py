#Attached: HW_5a, 5b, 5c, 5d
# ===================================================
#Program: HW_5b (Insurance)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user for the replacement 
# cost of a building then display the insurance
# ===================================================

REPLACE_PERCENT = 0.8

def showInsure(replace, minInsure):
    print(f"Replacement cost: ${replace:,.2f}")
    print(f"Percent insured: {REPLACE_PERCENT * 100:.2f}%")
    print(f"Minimum insurance: ${minInsure:,.2f}")

def main():
    replace = float(input("Enter the replacement amount: "))
    minInsure = replace * REPLACE_PERCENT
    showInsure(replace, minInsure)

if __name__ == "__main__":
    main()
    

# ===================================================
"""
OUTPUT
Enter the replacement amount: 837382.12 
Replacement cost: $837,382.12
Percent insured: 80.00%
Minimum insurance: $669,905.70

"""
# ===================================================