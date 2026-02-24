# -------------------------------------------------
# Program Name : Merge Two Lists & Remove Duplicates
# -------------------------------------------------

list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

merged_list = list1 + list2
result = []

# Removing duplicates
for num in merged_list:
    if num not in result:
        result.append(num)

print("Merged list without duplicates:", result)


#     output:
#           Enter first list elements: 1 2 3 4
#           Enter second list elements: 3 4 5 6
#           Merged list without duplicates: [1, 2, 3, 4, 5, 6]