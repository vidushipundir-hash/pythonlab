# -------------------------------------------------
# Program Name : Largest Element in List
# -------------------------------------------------

numbers = list(map(int, input("Enter elements: ").split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element is:", largest)

#   output:
#         Enter elements: 5 10 3 8 20
#         Largest element is: 20