# Program 9: Attendance System

# List of students present
present = ["Aman", "Riya", "Aman", "Karan"]

# Tuple of all students
all_students = ("Aman", "Riya", "Karan", "Sita")

# Set of unique present students
unique_present = set(present)

# Dictionary to mark attendance
attendance = {}

for student in all_students:
    attendance[student] = student in unique_present

print("Attendance Record:", attendance)