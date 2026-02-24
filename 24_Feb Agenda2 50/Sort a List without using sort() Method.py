# -------------------------------------------------
# Program Name : Sort List without sort()
# Description  : Using simple Bubble Sort
# -------------------------------------------------

numbers = list(map(int, input("Enter elements: ").split()))

n = len(numbers)

# Bubble Sort Algorithm
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("Sorted list:", numbers)

#     output:
#            Enter elements: 5 2 8 1 9
#            Sorted list: [1, 2, 5, 8, 9]