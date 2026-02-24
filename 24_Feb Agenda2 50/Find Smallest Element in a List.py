# -------------------------------------------------
# Program Name : Smallest Element in List
# -------------------------------------------------

numbers = list(map(int, input("Enter elements: ").split()))

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest element is:", smallest)


#     output:
#        Enter elements: 5 10 3 8 20
#        Smallest element is: 3