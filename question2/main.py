# Employee Class
class Employee:
    def __init__(self, employee_id, name, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.role = role
        self.salary = int(salary)

    def display_details(self):
        return f"{self.employee_id} - {self.name} - {self.role} - ₹{self.salary:.0f}"

# Function to add employee details to file
def add_employee(employee):
    with open("employees.txt", "a") as file:
        file.write(
            f"{employee.employee_id},{employee.name},{employee.role},{employee.salary}\n"
        )

# Function to read employees from file
def read_employees():
    employees = []

    try:
        with open("employees.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 4:
                    employee = Employee(
                        data[0], data[1], data[2], data[3]
                    )
                    employees.append(employee)

    except FileNotFoundError:
        print("Error: employees.txt file does not exist.")

    return employees

# Function to find employee with highest salary
def find_highest_salary(employees):
    return max(employees, key=lambda emp: emp.salary)

# Function to find employees by role
def find_employees_by_role(employees):
    role_count = {}

    for emp in employees:
        role_count[emp.role] = role_count.get(emp.role, 0) + 1

    return role_count

# Create file and store sample data
sample_employees = [
    Employee(101, "Rahul", "Python Developer", 50000),
    Employee(102, "Anjali", "Tester", 45000),
    Employee(103, "John", "Developer", 60000),
    Employee(104, "Priya", "Tester", 48000),
]

# Write data to file
with open("employees.txt", "w") as file:
    pass

for emp in sample_employees:
    add_employee(emp)

# Read employee data
employees = read_employees()
print("\n===== Employee Details =====\n")

for emp in employees:
    print(emp.display_details())

print("\n===== Employees with Salary>50000 =====\n")

high_salary_employees = [emp for emp in employees if emp.salary > 50000]

for emp in high_salary_employees:
    print(f"{emp.name} - ₹{emp.salary:.0f}")

highest_paid = find_highest_salary(employees)
print("\nHighest Paid Employee:\n")
print(f"{highest_paid.name} - ₹{highest_paid.salary:.0f}")

print("\nEmployee Count by Role:\n")
role_counts = find_employees_by_role(employees)

for role, count in role_counts.items():
    print(f"{role}: {count}")