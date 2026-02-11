#Attached: HW_5a, 5b, 5c, 5d
# ===================================================
#Program: HW_5d (Test Average and Grade)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user for two integers
# and return the greater value of the two
# ===================================================

def calc_average(scores):
    return sum(scores) / len(scores)

def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    scores = []
    for i in range(1, 6):
        score = float(input(f"Enter score {i}: "))
        scores.append(score)

    print("Score Numeric Grade Letter Grade")
    print("----------------------------------")
    for i, score in enumerate(scores, 1):
        grade = determine_grade(score)
        print(f"score {i}: {score} {grade}")

    average_score = calc_average(scores)
    average_grade = determine_grade(average_score)
    print(f"Average score: {average_score} \t {average_grade}")

if __name__ == "__main__":
    main()


# ===================================================
"""
OUTPUT
nter score 1: 88
Enter score 2: 79
Enter score 3: 90
Enter score 4: 79
Enter score 5: 93
Score Numeric Grade Letter Grade
----------------------------------
score 1: 88.0 B
score 2: 79.0 C
score 3: 90.0 A
score 4: 79.0 C
score 5: 93.0 A
Average score: 85.8      B

"""
# ===================================================