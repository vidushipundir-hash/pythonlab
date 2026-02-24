# Problem 96: Find first non-repeating character

# Taking input
string = input("Enter a string: ")

# Checking each character
for ch in string:
    if string.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found")


#      output:
#         Enter a string: swiss
#            First non-repeating character: w