# Problem 93: Replace all vowels with *

# Taking input
string = input("Enter a string: ")

vowels = "aeiouAEIOU"
new_string = ""

# Replacing vowels
for ch in string:
    if ch in vowels:
        new_string += "*"
    else:
        new_string += ch

# Printing result
print("Modified string:", new_string)


#    output:
#         Enter a string: Python Programming
#         Modified string: Pyth*n Pr*gr*mm*ng