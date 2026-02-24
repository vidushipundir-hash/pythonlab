# -------------------------------------------------
# Program Name : GCD using Function
# -------------------------------------------------

# Function to find GCD
def find_gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

# Taking input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calling function
result = find_gcd(num1, num2)

print("GCD is:", result)


#   output:
#       Enter first number: 12
#       Enter second number: 18
#       GCD is: 6