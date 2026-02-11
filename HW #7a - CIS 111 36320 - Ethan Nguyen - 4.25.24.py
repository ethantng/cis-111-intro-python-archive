#Attached: HW_7a, 7b
# ===================================================
#Program: HW_7a (Average of Numbers)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user to input 10 integers
# into a .txt file and find the average
# ===================================================

with open('numbers.txt', 'w') as file:
    for i in range(10):
        num = input(f"Enter #{i + 1}: ")
        file.write(num + '\n')

try:
    file_name = input("Please enter the file name to open: ")

    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file.readlines()]

    print("Let's display the values:")
    for number in numbers:
        print(number)

    total = sum(numbers)
    average = total / len(numbers)

    print(f"The sum of all the values in the file is: {total}")
    print(f"The average of all the values in the file is: {average}")

    with open(file_name, 'a') as file:
        file.write(f"The sum of all the values in the file is: {total}\n")
        file.write(f"The average of all the values in the file is: {average}\n")

except FileNotFoundError:
    print("Sorry, file not found.")



# ===================================================
"""
OUTPUT
Enter #1: 1
Enter #2: 2
Enter #3: 3
Enter #4: 4
Enter #5: 5
Enter #6: 6
Enter #7: 7
Enter #8: 8
Enter #9: 9
Enter #10: 10
Please enter the file name to open: numbers.txt
Let's display the values:
1
2
3
4
5
6
7
8
9
10
The sum of all the values in the file is: 55
The average of all the values in the file is: 5.5

"""
# ===================================================