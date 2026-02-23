# Online Exam Result Processor

scores = [25, 30, 34, 50, 60, 45, 20, 70]

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

# Add grace marks
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Count passed students
passed = 0
for s in scores:
    if s >= 40:
        passed += 1

print("Updated Scores:", scores)
print("Number of Students Passed:", passed)