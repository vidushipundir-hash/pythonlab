
# Taking input from user
num = int(input("Enter a number: "))

# Store original number (optional)
original_num = num

# Variable to store sum
sum_digits = 0

# Loop until number becomes 0
while num > 0:
    digit = num % 10        # Get last digit
    sum_digits += digit     # Add digit to sum
    num = num // 10         # Remove last digit

# Print result
print("Sum of digits =", sum_digits)


#-------------------------******----------------------******----------------------------

            #input:
                    #Enter a number: 65

            #output:      
                    #Sum of digits = 11

#-------------------------******----------------------******----------------------------

