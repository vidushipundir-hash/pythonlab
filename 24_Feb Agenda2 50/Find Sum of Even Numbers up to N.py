
# Taking input from user
n = int(input("Enter the value of N: "))

# Initialize variables
i = 1
even_sum = 0

# Using while loop to check numbers from 1 to N
while i <= n:
    
    # Check if number is even
    if i % 2 == 0:
        even_sum += i   # Add even number to sum
    
    i += 1   # Increment counter

# Display result
print("Sum of even numbers up to", n, "is:", even_sum)


#-----------------*********-----------------**********-----------------

#     input:
#            Enter the value of N: 8

#     output:
#             Sum of even numbers up to 8 is: 20

#------------------*********-----------------**********-----------------            