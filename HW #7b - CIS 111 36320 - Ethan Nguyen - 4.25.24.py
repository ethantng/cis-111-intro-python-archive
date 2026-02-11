#Attached: HW_7a, 7b
# ===================================================
#Program: HW_7b (Total Sales)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user to input the sales
# for the week and print the sum of the sales
# ===================================================

sales = []

for day in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
    sale_amount = float(input(f"Enter the sales for {day}: "))
    sales.append(sale_amount)

total_sales = sum(sales)

print(f"Total sales for the week: ${total_sales:.2f}")




# ===================================================
"""
OUTPUT
Enter the sales for Sunday: 10
Enter the sales for Monday: 20
Enter the sales for Tuesday: 30
Enter the sales for Wednesday: 40
Enter the sales for Thursday: 50
Enter the sales for Friday: 60
Enter the sales for Saturday: 70
Total sales for the week: $280.00

"""
# ===================================================