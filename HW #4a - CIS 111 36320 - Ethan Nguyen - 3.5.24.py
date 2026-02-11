#Attached: HW_4a, 4b, 4c, 4d
# ===================================================
#Program: HW_4a (Travel)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program calculates the distance a vehicle has
# traveled
# ===================================================

speed = int(input("What is the speed of the vehicle in mph? "))
hours = float(input("How many hours has it traveled? "))
print("\n")

print("Hour\tDistance Traveled")
print("-------------------------")
for i in range(1, int(hours) + 1):
    distance = speed * i
    print(f"{i:<20} {distance}")
    
if hours % 1 != 0:
    distance = speed * hours
    print(f"{hours:<20} {distance}")

# ===================================================
"""
OUTPUT
What is the speed of the vehicle in mph? 55
How many hours has it traveled? 6


Hour    Distance Traveled
-------------------------
1                    55
2                    110
3                    165
4                    220
5                    275
6                    330

"""
# ===================================================

