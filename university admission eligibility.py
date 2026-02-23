marks = 82
maths = True
entrance_score = 85

if marks < 75:
    print("Not Eligible: Less than 75% in 12th")
elif not maths:
    print("Not Eligible: Mathematics not studied")
elif entrance_score < 80:
    print("Not Eligible: Entrance score below 80")
else:
    print("Eligible for Admission")