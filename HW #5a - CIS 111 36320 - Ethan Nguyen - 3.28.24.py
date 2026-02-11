#Attached: HW_5a, 5b, 5c, 5d
# ===================================================
#Program: HW_5a (Converter)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user for the number of 
# kilometers and convert to miles
# ===================================================

KILOMETERS_TO_MILES = 0.6214

def showMiles(kilometers):
    miles = kilometers * KILOMETERS_TO_MILES
    print(f"The conversion of {kilometers:.2f} kilometers to miles is {miles:.2f} miles.")

def main():
    kilometers = float(input("Enter the distance in kilometers: "))
    showMiles(kilometers)

if __name__ == "__main__":
    main()
    

# ===================================================
"""
OUTPUT
Enter the distance in kilometers: 433
The conversion of 433.00 kilometers to miles is 269.07 miles.

"""
# ===================================================