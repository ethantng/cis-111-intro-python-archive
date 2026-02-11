#Attached: HW_3a, 3b, 3c, 3d
# ===================================================
#Program: HW_3d (Shipping Charges)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program asks the user for the weight of the
# package and determines the shipping charge
# ===================================================

weight = float(input("Enter the weight of the package: "))

if weight <= 2:
    rate_per_pound = 1.50
elif weight <= 6:
    rate_per_pound = 3.00
elif weight <= 10:
    rate_per_pound = 4.00
else:
    rate_per_pound = 4.75

    shipping_charges = rate_per_pound
    
    print(f"Shipping charge: ${shipping_charges:.2f}")
    

# ===================================================
"""
OUTPUT
Enter the weight of the package: 28
Shipping charge: $4.75

"""
# ===================================================
