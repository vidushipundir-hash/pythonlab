rating = 4
experience = 6
attendance = 92

increment = 0

if rating >= 4 and experience >= 5 and attendance >= 90:
    increment = 20
elif rating >= 3:
    increment = 10
else:
    increment = 5

print("Increment Percentage =", increment, "%")