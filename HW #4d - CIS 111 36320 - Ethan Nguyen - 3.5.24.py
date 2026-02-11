#Attached: HW_4a, 4b, 4c, 4d
# ===================================================
#Program: HW_4b (Rain)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program uses a nested loop to collect data
# and calculate the average rainfall over a year
# ===================================================

totmonths = 0
totrainfall = 0 

years = int(input("Enter the number of years: "))
for year in range(1, years + 1):
    print(f"For year {year}:")
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall amount for the month {month}: "))
        totmonths += 1
        totrainfall += rainfall
    
avgrainfall = totrainfall / totmonths

print(f"For {totmonths} months")
print(f"Total rainfall: {totrainfall:.2f} inches")
print(f"Average monthly rainfall: {avgrainfall:.2f} inches")

# ===================================================
"""
OUTPUT
Enter the number of years: 1
For year 1:
Enter the rainfall amount for the month 1: 2
Enter the rainfall amount for the month 2: 2
Enter the rainfall amount for the month 3: 2
Enter the rainfall amount for the month 4: 2
Enter the rainfall amount for the month 5: 2
Enter the rainfall amount for the month 6: 2
Enter the rainfall amount for the month 7: 2
Enter the rainfall amount for the month 8: 2
Enter the rainfall amount for the month 9: 2
Enter the rainfall amount for the month 10: 2
Enter the rainfall amount for the month 11: 2
Enter the rainfall amount for the month 12: 2
For 12 months
Total rainfall: 24.00 inches
Average monthly rainfall: 2.00 inches

"""
# ===================================================

