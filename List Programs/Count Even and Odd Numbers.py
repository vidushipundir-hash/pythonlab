# -------------------------------------------------
# Program Name : Count Even and Odd Numbers
# Description  : This program counts even and
#                odd numbers in a list.
# -------------------------------------------------

# Creating a list
numbers = [12, 7, 9, 20, 33, 40]

# Initializing counters
even_count = 0
odd_count = 0

# Using loop
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display result
print("List Elements :", numbers)
print("Even Numbers :", even_count)
print("Odd Numbers :", odd_count)