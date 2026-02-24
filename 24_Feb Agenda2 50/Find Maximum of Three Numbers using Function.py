# -------------------------------------------------
# Program Name : Maximum of Three Numbers
# -------------------------------------------------

# Function to find maximum
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Taking input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

# Calling function
maximum = find_max(x, y, z)

print("Maximum number is:", maximum)

#   output:
#  Enter first number: 10
#  Enter second number: 25
#  Enter third number: 15
#  Maximum number is: 25