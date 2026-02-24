# Problem 97: Count uppercase and lowercase letters

# Taking input
string = input("Enter a string: ")

upper = 0
lower = 0

# Counting letters
for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

# Printing result
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


#    output:
#        Enter a string: Python Is Easy
#          Uppercase letters: 3
#          Lowercase letters: 9