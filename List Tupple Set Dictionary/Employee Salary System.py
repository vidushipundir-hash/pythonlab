# Program 4: Employee Salary System

# List of employees
employees = ["Rahul", "Sneha", "Arjun"]

# Tuple of departments
departments = ("HR", "IT", "Finance")

# Dictionary of salaries
salary = {
    "Rahul": 30000,
    "Sneha": 40000,
    "Arjun": 50000
}

# Set for high salary employees
high_salary = set()

for emp in employees:
    if salary[emp] > 35000:
        high_salary.add(emp)

print("Departments:", departments)
print("High Salary Employees:", high_salary)