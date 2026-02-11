#Attached: HW_8a, 8b, 8c
# ===================================================
#Program: HW_8a (Number)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user to input an array of 
# 20 numbers and will return the high, low, total,
# and average of those numbers
# ===================================================

num = []

for i in range(1, 21):
    numin = float(input(f"Enter number {i} of 20: ")) #int
    num.append(numin)

low = min(num)
high = max(num)
tot = sum(num)
avg = tot / len(num)

print(f"Low: {low:,.2f}")
print(f"High: {high:,.2f}")
print(f"Total: {tot:,.2f}")
print(f"Average: {avg:,.2f}")


# ===================================================
"""
OUTPUT
Enter number 1 of 20: 2
Enter number 2 of 20: 4
Enter number 3 of 20: 3
Enter number 4 of 20: 4
Enter number 5 of 20: 2
Enter number 6 of 20: 3
Enter number 7 of 20: 4
Enter number 8 of 20: 6
Enter number 9 of 20: 4
Enter number 10 of 20: 3
Enter number 11 of 20: 4
Enter number 12 of 20: 2
Enter number 13 of 20: 1
Enter number 14 of 20: 6
Enter number 15 of 20: 4
Enter number 16 of 20: 5
Enter number 17 of 20: 3
Enter number 18 of 20: 6
Enter number 19 of 20: 3
Enter number 20 of 20: 4
Low: 1.00
High: 6.00
Total: 73.00
Average: 3.65

"""
# ===================================================
