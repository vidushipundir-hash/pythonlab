# -------------------------------------------------
# Program Name : Remove Duplicates from List
# -------------------------------------------------

numbers = list(map(int, input("Enter elements: ").split()))

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List after removing duplicates:", result)


#   output;
#        Enter elements: 1 2 2 3 4 4 5
#        List after removing duplicates: [1, 2, 3, 4, 5]