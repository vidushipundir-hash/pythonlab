# -------------------------------------------------
# Program Name : Check Unique Elements in Tuple
# -------------------------------------------------

numbers = tuple(map(int, input("Enter elements: ").split()))

unique = True

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            unique = False
            break
    if not unique:
        break

if unique:
    print("All elements in tuple are unique")
else:
    print("Tuple contains duplicate elements")


#     output:
#            Enter elements: 1 2 3 4 5
#            All elements in tuple are unique