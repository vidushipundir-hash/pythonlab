# Problem 95: Remove duplicate characters from string

# Taking input
string = input("Enter a string: ")

result = ""

# Removing duplicates
for ch in string:
    if ch not in result:
        result += ch

# Printing result
print("String after removing duplicates:", result)


#     output:
#            Enter a string: programming
#            String after removing duplicates: progamin