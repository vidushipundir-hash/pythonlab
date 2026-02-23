# Program 1: Student Marks Management

# List of student names
students = ["Aman", "Riya", "Karan"]

# Tuple of subjects (fixed)
subjects = ("Math", "Science", "English")

# Dictionary to store marks
marks = {
    "Aman": [85, 90, 88],
    "Riya": [78, 82, 80],
    "Karan": [92, 89, 94]
}

# Set to store unique passed students
passed_students = set()

# Checking average marks
for name in students:
    avg = sum(marks[name]) / len(subjects)
    if avg >= 40:
        passed_students.add(name)

print("Passed Students:", passed_students)