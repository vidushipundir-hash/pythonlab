# -------------------------------------------------
# Program Name : Second Largest Element in List
# -------------------------------------------------

# Taking input (space separated numbers)
numbers = list(map(int, input("Enter elements: ").split()))

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest element is:", second_largest)


#    output:
#         Enter elements: 5 10 3 8 20
#         Second largest element is: 10