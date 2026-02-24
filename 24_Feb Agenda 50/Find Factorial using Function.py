# -------------------------------------------------
# Program Name : Factorial using Function
# -------------------------------------------------

# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


# Taking input
num = int(input("Enter a number: "))

# Calling function
result = factorial(num)

print("Factorial of", num, "is:", result)

#   output:
# Enter a number: 6
# Factorial of 6 is: 720