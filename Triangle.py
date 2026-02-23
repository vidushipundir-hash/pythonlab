# Program to find the third angle of a triangle

# Input first two angles
angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))

# Sum of angles in a triangle is always 180 degrees
sum_of_angles = angle1 + angle2

# Check if the given angles are valid
if sum_of_angles < 180 and angle1 > 0 and angle2 > 0:
    
    # Calculate third angle
    angle3 = 180 - sum_of_angles
    
    print("Third angle of the triangle is:", angle3)

else:
    print("Invalid angles! Sum must be less than 180 and greater than 0.")
