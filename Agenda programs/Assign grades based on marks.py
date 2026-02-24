
# Taking input from user
marks = int(input("Enter your marks: "))

# Checking grade conditions
if marks >= 90 and marks <= 100:
    print("Grade: A")

elif marks >= 75 and marks < 90:
    print("Grade: B")

elif marks >= 60 and marks < 75:
    print("Grade: C")

elif marks >= 50 and marks < 60:
    print("Grade: D")

elif marks >= 0 and marks < 50:
    print("Grade: F")

else:
    print("Invalid Marks")


#----------------------******----------------******--------------------  

#           input:
#                 Enter your marks: 82

#           output:
#                  Grade: B

#----------------------******----------------******--------------------  