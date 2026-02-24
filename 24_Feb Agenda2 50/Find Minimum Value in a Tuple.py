# -------------------------------------------------
# Program Name : Minimum Value in Tuple
# -------------------------------------------------

numbers = tuple(map(int, input("Enter elements: ").split()))

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum value in tuple is:", minimum)


#    output:
#            Enter elements: 5 10 3 8 20
#            Minimum value in tuple is: 3