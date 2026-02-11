#Attached: HW_8a, 8b, 8c
# ===================================================
#Program: HW_8b (Rainfall)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user to input the rainfall
# for each month of the year, then return the average,
# high, and low
# ===================================================

rainfall = []
months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

for month in months:
    rain = float(input(f"Enter the rainfall for {month}: "))
    rainfall.append(rain)
    
tot_rainfall = sum(rainfall)
avg_rainfall = tot_rainfall / len(rainfall)
high_rainfall = months[rainfall.index(max(rainfall))]
low_rainfall = months[rainfall.index(min(rainfall))]

print(f"Total rainfall: {tot_rainfall:.2f}")
print(f"Average rainfall: {avg_rainfall:.2f}")
print(f"Highest rainfall: {high_rainfall}")
print(f"Lowest rainfall: {low_rainfall}")


# ===================================================
"""
OUTPUT
Enter the rainfall for January: 3.4
Enter the rainfall for February: 2.3
Enter the rainfall for March: 4.1 
Enter the rainfall for April: 1.3
Enter the rainfall for May: 1.1
Enter the rainfall for June: 2.6
Enter the rainfall for July: 4.2
Enter the rainfall for August: 3.3
Enter the rainfall for September: 4.4
Enter the rainfall for October: 1.1
Enter the rainfall for November: 2.2
Enter the rainfall for December: 3.1
Total rainfall: 33.10
Average rainfall: 2.76
Highest rainfall: September
Lowest rainfall: May

"""
# ===================================================
