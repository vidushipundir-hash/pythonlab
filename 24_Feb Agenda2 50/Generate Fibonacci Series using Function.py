# -------------------------------------------------
# Program Name : Fibonacci Series using Function
# -------------------------------------------------

# Function to generate Fibonacci series
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

# Taking input
terms = int(input("Enter number of terms: "))

# Calling function
fibonacci(terms)

#    output:
#        Enter number of terms: 6
#        0 1 1 2 3 5