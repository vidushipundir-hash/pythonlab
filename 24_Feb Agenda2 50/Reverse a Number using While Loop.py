
# Taking input from user
num = int(input("Enter a number: "))

# Store original number (optional)
original = num

# Variable to store reversed number
reverse = 0

# While loop to reverse the number
while num > 0:
    digit = num % 10          # Get last digit
    reverse = reverse * 10 + digit   # Add digit to reverse number
    num = num // 10           # Remove last digit

# Print result
print("Reversed Number:", reverse)


#---------------******----------------******--------------------

     #input: 12345

     #output: 54321

#-----------------******----------------******--------------------     