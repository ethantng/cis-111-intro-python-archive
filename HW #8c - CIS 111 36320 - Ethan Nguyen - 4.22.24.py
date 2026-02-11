#Attached: HW_8a, 8b, 8c
# ===================================================
#Program: HW_8c (Driver's License)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will scan through a .txt file for 
# "answers" and compare them to a set arrayy
# ===================================================

correct = [
    "A", "C", "A", "A", "D",
    "B", "C", "A", "C", "B",
    "A", "D", "C", "A", "D",
    "C", "B", "B", "D", "A"
]

numcorrect = 0
incorrect = 0
numincorrect = []

with open('Student_solution.txt', 'r') as file:
    answers = file.read().splitlines()

for i in range(len(correct)):
    if answers[i] == correct[i]:
        numcorrect += 1
    else:
        incorrect += 1
        numincorrect.append(i + 1)

if numcorrect >= 15:
    print("Congratulations! You passed the exam.")
else:
    print("You failed the exam.")
    
print("Number of questions you answered correctly:", numcorrect)
print("Number of questions you answered incorrectly:", incorrect)

print("Questions you answered incorrectly:", ', '.join(map(str, numincorrect)))


# ===================================================
"""
OUTPUT
Congratulations!! You passed the exam.
Number of questions you answered correctly: 16
Number of questions you answered incorrectly: 4
Questions you answered incorrectly: 17, 18, 19, 20

"""
# ===================================================
