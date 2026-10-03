#TASK 2 — Student ID Card
#Goal
#Practice storing and formatting different types of data.
#Create a program that generates a simple student ID card.
#Ask for:
#Student name
#Student ID
#Department
#Year
#University
#Phone number
#Display the information in a clean ID-card style.
#
#Example
#+--------------------------------+
#|       AKIBA STUDENT CARD       |
#+--------------------------------+
#| Name: Ahmed Ali                |
#| ID: AKB-001                    |
#| Department: Software Eng.      |
#| Year: 1                        |
#| University: Jimma University   |
#| Phone: 0912345678              |
#+--------------------------------+
#
#Concepts
#Variables • strings • integers • formatted output
#


line = "=============================================================="
student_full_name = input("Full Name: ")
student_id = input("ID: ")
department = input("Department: ")
year = input("Year: ")
university = input("University: ")
phone = input("Phone Number: ")

output = f"""
{line} \n
\t \tName: {student_full_name}
\t \tID: {student_id}
\t \tDepartment: {department}
\t \tYear: {year}
\t \tUniversity: {university}
\t \tPhone: {phone}
{line} \n  

    """
print(output)
