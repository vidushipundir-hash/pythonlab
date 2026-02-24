
# Taking input from user
num = int(input("Enter a number: "))

# Check for negative number
if num < 0:
    print("Factorial does not exist for negative numbers")

else:
    factorial = 1
    i = 1

    # While loop to calculate factorial
    while i <= num:
        factorial *= i
        i += 1

    print("Factorial of", num, "is:", factorial)


#-----------------******------------------******--------------------

#         input:
#                Enter a number: 5
       
#         output:   
#                 Factorial of 5 is: 120

#-----------------******------------------******--------------------
