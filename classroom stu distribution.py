# Classroom Student Distribution

total_students = 125
students_per_class = 30

# Calculate full classes
full_classes = total_students // students_per_class

# Calculate remaining students
remaining_students = total_students % students_per_class

# Display results
print("Number of full classes =", full_classes)
print("Remaining students without class =", remaining_students)