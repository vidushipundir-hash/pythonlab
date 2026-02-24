# Problem 99: Generate all substrings of a string

# Taking input
string = input("Enter a string: ")

print("Substrings are:")

# Generating substrings
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        print(string[i:j])


#   output:
#       Enter a string: abc
#       Substrings are:
#       a
#       ab
#       abc
#       b
#       bc
#       c