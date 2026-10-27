# Problem Statement
Question 2 — Simple Employee File Management
Scenario
You are working on a small Python application that maintains employee information. Employee details need to be stored in a file and later read to generate a simple report.
Requirements
9.	Create a file called employees.txt.
10.	Store employee details such as: Employee ID, Name, Role, and Salary.
11.	Read the employee information from the file.
12.	Display all employees.
13.	Find and display employees whose salary is greater than ₹50,000.
14.	Find the employee with the highest salary.
15.	Count how many employees belong to each role.
16.	Use functions such as add_employee(), read_employees(), find_highest_salary(), and find_employees_by_role().
17.	Use a context manager (with open()) while working with the file.
18.	Handle the situation where the file does not exist using exception handling.
19.	Create a simple Employee class with employee_id, name, role, and salary.
20.	Create a method such as display_details().
Sample Employee Data
101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000
Sample Output
===== Employee Details =====

101 - Rahul - Python Developer - ₹50000
102 - Anjali - Tester - ₹45000
103 - John - Developer - ₹60000
104 - Priya - Tester - ₹48000

===== Employees with Salary > 50000 =====

John - ₹60000

Highest Paid Employee:
John - ₹60000

Employee Count by Role:
Developer: 1
Python Developer: 1
Tester: 2

# Approach/logic used
List comprehension used for salary filtering
Exception Handling
File Creation
Context Manager and read data from the file
display_details() method
Class and Functions 
Loops
Dictionaries
Data Analysis
Store Employee Data in a File

# How to run the program
cd question2
python main.py

# Sample Input

101,Rahul,Python Developer,50000
102,Anjali,Tester,45000
103,John,Developer,60000
104,Priya,Tester,48000

# Sample Output

===== Employee Details =====

101 - Rahul - Python Developer - ₹50000
102 - Anjali - Tester - ₹45000
103 - John - Developer - ₹60000
104 - Priya - Tester - ₹48000

===== Employees with Salary>50000 =====

John - ₹60000

Highest Paid Employee:

John - ₹60000

Employee Count by Role:

Developer: 1
Python Developer: 1
Tester: 2

# Python concepts used

Constructor
File Handling
Exception Handling
Context Manager
Functions
Lists
Dictionaries
Loops
Lambda function
Built in functions
Class, method and objects


