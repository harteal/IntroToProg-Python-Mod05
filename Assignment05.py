# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
# Alex Harteloo, 2/9/24, Script Created
# ------------------------------------------------------------------------------------------ #

import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ''
file = None  # Holds a reference to an opened file.
menu_choice: str = '' # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data


# When the program starts, read the file data into a list of lists (table)
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except Exception as e:
    print("Error! Please check message below.")
    print(e)
    print(type(e))
    print(e.__doc__)
    print(e.__str__())

# Present and Process the data
while (True):
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        print("-" * 50)
        try:
            student_first_name = input("Enter the student's first name: ")
            student_last_name = input("Enter the student's last name: ")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            print("-" * 50)
        except Exception as e:
            print("Error! Please check message below.")
            print(e)
            print(type(e))
            print(e.__doc__)
            print(e.__str__())
        continue

    # Present the current data & custom message
    elif menu_choice == "2":
        try:
            print("-"*50)
            for student in students:
                print(f"{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
            continue
        except KeyError as e:
            print("Error! Please check message below.")
            print(e)
            print(type(e))
            print(e.__doc__)
            print(e.__str__())
            print('Check to make sure all keys match in database file. ')
        except Exception as e:
            print("Error! Please check message below.")
            print(e)
            print(type(e))
            print(e.__doc__)
            print(e.__str__())
        print("-" * 50)

    # Save the data to a file
    elif menu_choice == "3":
        try:
            print("-" * 50)
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
            print("-" * 50)
        except Exception as e:
            print("Error! Please check message below.")
            print(e)
            print(type(e))
            print(e.__doc__)
            print(e.__str__())
        continue

    # Stop the program
    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")