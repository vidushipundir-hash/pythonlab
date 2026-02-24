# -------------------------------------------------
# Program Name : Intersection of Two Sets
# -------------------------------------------------

set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Performing intersection
result = set1 & set2

print("Intersection of sets:", result)


#    output:
#           Enter first set elements: 1 2 3 4
#           Enter second set elements: 3 4 5 6
#           Intersection of sets: {3, 4}