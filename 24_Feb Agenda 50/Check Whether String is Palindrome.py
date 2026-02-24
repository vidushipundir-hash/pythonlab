# -------------------------------------------------
# Program Name : Check String Palindrome
# -------------------------------------------------

text = input("Enter a string: ")

reverse = ""

# Reversing string
for ch in text:
    reverse = ch + reverse

# Checking palindrome
if text == reverse:
    print("The string is a Palindrome")
else:
    print("The string is not a Palindrome")


#  output
#     Enter a string: madam
#     The string is a Palindrome