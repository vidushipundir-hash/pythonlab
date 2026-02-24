# -------------------------------------------------
# Program Name : Count Occurrence in Tuple
# -------------------------------------------------

numbers = tuple(map(int, input("Enter elements: ").split()))
element = int(input("Enter element to count: "))

count = 0

for num in numbers:
    if num == element:
        count += 1

print("Occurrence of", element, "is:", count)


#   output:
#         Enter elements: 1 2 2 3 4 2
#         Enter element to count: 2
#         Occurrence of 2 is: 3