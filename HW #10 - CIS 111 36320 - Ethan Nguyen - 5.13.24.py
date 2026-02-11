#Attached: HW_10
# ===================================================
#Program: HW_10 (Dictionaries)
# ===================================================
#Programmer: Ethan Nguyen
#Class: CIS_111 #36320 - Th 12:30 pm class
# ===================================================
#Description:
# The program will ask the user to input a course
# number then the program should display the course
# with its course details
# ===================================================

course_details = {
    "CS101": {"Room": "3004", "Instructor": "Haynes", "Time": "8:00 am"},
    "CS102": {"Room": "4501", "Instructor": "Alvarado", "Time": "9:00 am"},
    "CS103": {"Room": "6755", "Instructor": "Rich", "Time": "10:00 am"},
    "NT110": {"Room": "1244", "Instructor": "Burke", "Time": "11:00 am"},
    "CM241": {"Room": "1411", "Instructor": "Lee", "Time": "1:00 pm"}
}

course_number = input("Enter a course number: ")

if course_number.upper() in course_details:
    print(f"The details for course {course_number.upper()} are:")
    for key, value in course_details[course_number.upper()].items():
        print(f"{key}: {value}")
else:
    print("Course not found.")


# ===================================================
"""
OUTPUT
Enter a course number: CS102
The details for course CS102 are:
Room: 4501
Instructor: Alvarado
Time: 9:00 am

"""
# ===================================================



