# -------------------------------------------------
# Program Name : Count Frequency of Elements
# -------------------------------------------------

# Taking input
numbers = list(map(int, input("Enter elements: ").split()))

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency of elements:")
for key in frequency:
    print(key, ":", frequency[key])


#   output:
#           Enter elements: 1 2 2 3 4 4 4
#           Frequency of elements:
#           1 : 1
#           2 : 2
#           3 : 1
#         4 : 3