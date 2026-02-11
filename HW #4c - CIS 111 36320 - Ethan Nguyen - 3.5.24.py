#Attached: HW_4a, 4b, 4c, 4d
# ===================================================
#Program: HW_4c (Money)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program calculates the amount of money a person
# would earn over a period of time
# ===================================================

days = int(input("Enter the number of days: "))
totpay = 0

print("Day\tPennies")
print("--------------------")
for day in range(1, days + 1):
    pay = 0.01 * 2**(day - 1)
    totpay += pay
    print(f"{day}\t${pay:.2f}")

print(f"The total salary for {days} days is: ${totpay:.2f}")



# ===================================================
"""
OUTPUT
Enter the number of days: 15
Day     Pennies
--------------------
1       $0.01
2       $0.02
3       $0.04
4       $0.08
5       $0.16
6       $0.32
7       $0.64
8       $1.28
9       $2.56
10      $5.12
11      $10.24
12      $20.48
13      $40.96
14      $81.92
15      $163.84
The total salary for 15 days is: $327.67

"""
# ===================================================

