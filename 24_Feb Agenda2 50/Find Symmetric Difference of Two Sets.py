# -------------------------------------------------
# Program Name : Symmetric Difference of Two Sets
# -------------------------------------------------

set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Performing symmetric difference
result = set1 ^ set2

print("Symmetric difference:", result)


#    output:
#          Enter first set elements: 1 2 3
#          Enter second set elements: 3 4 5
#          Symmetric difference: {1, 2, 4, 5}