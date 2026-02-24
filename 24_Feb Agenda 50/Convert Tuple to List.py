# -------------------------------------------------
# Program Name : Convert Tuple to List
# -------------------------------------------------

numbers = tuple(map(int, input("Enter elements: ").split()))

# Converting tuple to list
converted_list = list(numbers)

print("Converted list:", converted_list)


#   output:
#          Enter elements: 1 2 3 4
#          Converted list: [1, 2, 3, 4]