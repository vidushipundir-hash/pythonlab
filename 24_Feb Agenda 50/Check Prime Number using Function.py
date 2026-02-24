# -------------------------------------------------
# Program Name : Check Prime using Function
# -------------------------------------------------

# Function to check prime
def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True


# Taking input
number = int(input("Enter a number: "))

# Calling function
if is_prime(number):
    print(number, "is a Prime number")
else:
    print(number, "is not a Prime number")

#   output:
#    Enter a number: 7
#    7 is a Prime number
