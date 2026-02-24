# -------------------------------------------------
# Program Name : Power using Recursion
# -------------------------------------------------

# Recursive function
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

# Taking input
b = int(input("Enter base: "))
e = int(input("Enter exponent: "))

# Calling function
result = power(b, e)

print(b, "raised to", e, "is:", result)

#   output:
#       Enter base: 3
#       Enter exponent: 4
#       3 raised to 4 is: 81