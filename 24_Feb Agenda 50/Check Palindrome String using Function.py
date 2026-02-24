# -------------------------------------------------
# Program Name : Check Palindrome String
# -------------------------------------------------

# Function to check palindrome
def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

# Taking input
string = input("Enter a string: ")

# Calling function
if is_palindrome(string):
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")

#   output:
#  Enter a string: madam
#  The string is a Palindrome
