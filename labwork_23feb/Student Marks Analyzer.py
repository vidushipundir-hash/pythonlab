# Student Marks Analyzer

marks = [95, 67, 120, -5, 88, 76, 54, 101, 89]

# Remove invalid marks
valid_marks = []
for m in marks:
    if 0 <= m <= 100:
        valid_marks.append(m)

print("Valid Marks:", valid_marks)

# Calculate average
average = sum(valid_marks) / len(valid_marks)
print("Average Marks:", average)

# Find topper(s)
top_score = max(valid_marks)
print("Topper Score:", top_score)

# Display grade based on average
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)