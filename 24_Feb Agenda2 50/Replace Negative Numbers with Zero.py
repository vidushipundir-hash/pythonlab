# -------------------------------------------------
# Program Name : Replace Negative Numbers with Zero
# -------------------------------------------------

numbers = list(map(int, input("Enter elements: ").split()))

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print("Updated list:", numbers)

#    output:
#           Enter elements: 5 -3 8 -1 2
#           Updated list: [5, 0, 8, 0, 2]