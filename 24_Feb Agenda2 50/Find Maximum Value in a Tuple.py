# -------------------------------------------------
# Program Name : Maximum Value in Tuple
# -------------------------------------------------

# Taking input (space separated values)
numbers = tuple(map(int, input("Enter elements: ").split()))

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum value in tuple is:", maximum)

#   output:
#         Enter elements: 5 10 3 8 20
#         Maximum value in tuple is: 20