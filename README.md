# Problem Statement
Question 1 — Student Marks Management System
Scenario
You are asked to develop a simple Python program to manage student marks. The program should accept details of multiple students, calculate their results, and display a summary.
Requirements
1.	Store the following information for each student: Student ID, Student Name, Python Marks, SQL Marks, and AI Marks.
2.	Calculate Total Marks, Average Marks, and Grade.
3.	Display whether the student is PASS (average >= 40) or FAIL (average < 40).
4.	Display the student who has the highest average.
5.	Display the list of students who scored more than 75 average marks.
6.	Use appropriate Lists, Dictionaries, Functions, Conditional Statements, and Loops.
7.	Use at least one List Comprehension.
8.	Display the final result in a readable format.
Sample Output
===== Student Result =====

Student ID: 101
Name: Rahul
Total: 240
Average: 80
Grade: A
Result: PASS

Student ID: 102
Name: Anjali
Total: 195
Average: 65
Grade: B
Result: PASS

Highest Scoring Student: Rahul
Students above 75: Rahul, Priya

# Approach/logic used
Collect student data
Store data using Dictionary
Calculate results and determine Pass/Fail
Display Student details through list.
Find highest scoring student
Used List Comprehension to filter students above 75 Average.

# How to run the program
cd question1
python main.py

# Sample Input
Enter number of students: 4

Enter details for Student 1
Student ID: 100
Student Name: Aleena
Python Marks: 55
SQL Marks: 67
AI Marks: 43

Enter details for Student 2
Student ID: 101
Student Name: Biju
Python Marks: 78
SQL Marks: 98
AI Marks: 32

Enter details for Student 3
Student ID: 102
Student Name: Jithin
Python Marks: 33
SQL Marks: 43
AI Marks: 12

Enter details for Student 4
Student ID: 104
Student Name: Keenu
Python Marks: 77
SQL Marks: 85
AI Marks: 99

# Sample Output
======= Student Result ======
Student ID : 100
Name       : Aleena
Total      : 165
Average    : 55
Grade      : C
Result     : PASS

======= Student Result ======
Student ID : 101
Name       : Biju
Total      : 208
Average    : 69
Grade      : B
Result     : PASS

======= Student Result ======
Student ID : 102
Name       : Jithin
Total      : 88
Average    : 29
Grade      : F
Result     : FAIL

======= Student Result ======
Student ID : 104
Name       : Keenu
Total      : 261
Average    : 87
Grade      : A+
Result     : PASS

================================
Highest Scoring Student : Keenu
Students above 75:
Keenu

# Python Concepts Used
Variables
Lists
Dictionaries
Conditional Statements
Lambda Function
Built-in Functions
Operators
Data Structures
List Comprehension
Loops
Functions

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
Enter number of employees: 3

Enter Employee 1 Details
Employee ID: 101
Name: Rahul
Role: Python Developer
Salary: 50000

Enter Employee 2 Details
Employee ID: 102
Name: Anjali
Role: Tester
Salary: 45000

Enter Employee 3 Details
Employee ID: 103
Name: John
Role: Developer
Salary: 60000


# Sample Output

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
