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
