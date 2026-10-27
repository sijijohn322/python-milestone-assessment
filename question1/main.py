# Function to calculate grade
def calculate_grade(avg):
    if avg >= 85:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"

# Function to display student details
def display_student(student):
    print("\n======= Student Result ======")
    print("Student ID :", student["id"])
    print("Name       :", student["name"])
    print("Total      :", student["total"])
    print("Average    :", round(student["average"], 2))
    print("Grade      :", student["grade"])
    print("Result     :", student["result"])

# Main Program
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for Student {i+1}")

    sid = int(input("Student ID: "))
    name = input("Student Name: ")
    python_marks = int(input("Python Marks: "))
    sql_marks = int(input("SQL Marks: "))
    ai_marks = int(input("AI Marks: "))

    total = python_marks + sql_marks + ai_marks
    average = int(total / 3)
    grade = calculate_grade(average)
    result = "PASS" if average >= 40 else "FAIL"

    student = {
        "id": sid,
        "name": name,
        "python": python_marks,
        "sql": sql_marks,
        "ai": ai_marks,
        "total": total,
        "average": average,
        "grade": grade,
        "result": result
    }

    students.append(student)

# Display all student results
print("\n\n******** FINAL RESULTS ********")

for student in students:
    display_student(student)

# Find highest scoring student
highest_student = max(students, key=lambda x: x["average"])
print("\n================================")
print("Highest Scoring Student :", highest_student["name"])

# List comprehension for students with average > 75
top_students = [student["name"] for student in students if student["average"] > 75]

print("Students above 75:")
if top_students:
    print(", ".join(top_students))
else:
    print("No students scored above 75.")