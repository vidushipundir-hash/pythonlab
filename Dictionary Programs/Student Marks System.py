# Program 1: Student Marks System using Dictionary

# Creating dictionary of students and their marks
students = {
    "Aman": 85,
    "Riya": 90,
    "Karan": 78,
    "Sneha": 88
}

# Display all students with marks
print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

# Find topper
topper = max(students, key=students.get)
print("Topper is:", topper)