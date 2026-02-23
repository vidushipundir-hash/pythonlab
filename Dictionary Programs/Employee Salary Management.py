# Program 4: Employee Salary Management

# Dictionary storing employee salary
salary = {
    "Rahul": 30000,
    "Sneha": 45000,
    "Arjun": 50000
}

# Increase salary by 10%
for emp in salary:
    salary[emp] = salary[emp] * 1.10

# Display updated salary
print("Updated Salary List:")
for emp, sal in salary.items():
    print(emp, ":", sal)