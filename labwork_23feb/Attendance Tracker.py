# Attendance Tracker

attendance = [1, 1, 0, 0, 1, 0, 1, 1, 0, 1]

total_days = len(attendance)
present_days = attendance.count(1)

percentage = (present_days / total_days) * 100
print("Attendance Percentage:", percentage)

if percentage < 75:
    print("Warning: Below 75% attendance")

# Replace consecutive absences
for i in range(len(attendance) - 1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = "Warning"

print("Updated Attendance:", attendance)