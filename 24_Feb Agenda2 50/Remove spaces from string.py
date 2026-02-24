# Problem 90: Remove spaces from string

# Taking input
string = input("Enter a string: ")

# Removing spaces
new_string = ""

for ch in string:
    if ch != " ":
        new_string += ch

# Printing result
print("String without spaces:", new_string)

#   output:
#       Enter a string: Python is easy
#       String without spaces: Pythoniseasy