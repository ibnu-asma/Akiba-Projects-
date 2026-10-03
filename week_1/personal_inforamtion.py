
# TASK 1 — Personal Introduction
# Goal
#Practice variables, strings, and user input.
#Create a program that asks the user for:
#Full name
#Age
#City
#University
#Department
#Favorite programming language
#One programming goal
#Display the information as a professional introduction.
#Example
#========================================
#        STUDENT INTRODUCTION
#========================================
#
#My name is Ahmed Ali.
#I am 21 years old.
#I live in Addis Ababa.
#I study Software Engineering at Jimma University.
#My favorite programming language is Python.
#
#My programming goal:
#Become a professional backend developer.
#
#

full_name = input("Enter your full name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
universtiy = input("Enter your universtiy: ")
department = input("Enter your department: ")
goal = input("Your goal: ")
programing_language = input("Your Programming Language: ")

line = "========================================"
output = f"""
{line} \n
\t \t STUDENT INFORMATION
{line} \n
\t My name is {full_name}.
\t I am {age} years old.
\t I live in {city}.
\t I study {department} at {universtiy}.
\t My favorite programming language is {programing_language}.
\t My My professional goal is to become {goal}

{line} \n 
         """
print(output)

