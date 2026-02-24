
# Taking input from user
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculate BMI
bmi = weight / (height * height)

# Display BMI value
print("Your BMI is:", round(bmi, 2))

# Check BMI category
if bmi < 18.5:
    print("Category: Underweight")

elif bmi >= 18.5 and bmi < 25:
    print("Category: Normal weight")

elif bmi >= 25 and bmi < 30:
    print("Category: Overweight")

else:
    print("Category: Obese")


#----------------------******----------------******--------------------  
# 
#           input:
#                   Enter weight in kg: 56
#                   Enter height in meters: 29
#           output:
#                   Your BMI is: 0.07
#                   Category: Underweight
 
# #----------------------******----------------******--------------------      