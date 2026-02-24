# -------------------------------------------------
# Program Name : Student Marks & Find Topper
# -------------------------------------------------

# Taking number of students
n = int(input("Enter number of students: "))

marks = {}

# Taking student name and marks
for i in range(n):
    name = input("Enter student name: ")
    score = int(input("Enter marks: "))
    marks[name] = score

# Finding topper
topper = max(marks, key=marks.get)

print("Topper is:", topper)
print("Marks:", marks[topper])



#      output:
#           Enter number of students: 3
#           Enter student name: Ravi
#           Enter marks: 85
#           Enter student name: Anjali
#           Enter marks: 92
#           Enter student name: Mohan
#           Enter marks: 88
#           Topper is: Anjali
#           Marks: 92