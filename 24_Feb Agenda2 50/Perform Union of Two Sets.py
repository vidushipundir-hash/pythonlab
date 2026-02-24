# -------------------------------------------------
# Program Name : Union of Two Sets
# -------------------------------------------------

# Taking input (space separated values)
set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Performing union
result = set1 | set2

print("Union of sets:", result)


#      output:
#             Enter first set elements: 1 2 3 4
#             Enter second set elements: 3 4 5 6
#             Union of sets: {1, 2, 3, 4, 5, 6}