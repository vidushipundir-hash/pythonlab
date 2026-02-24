# -------------------------------------------------
# Program Name : Rotate List by K Positions
# -------------------------------------------------

numbers = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter value of K: "))

n = len(numbers)
k = k % n   # Handle large K values

rotated = numbers[k:] + numbers[:k]

print("Rotated list:", rotated)


#       output:
#             Enter elements: 1 2 3 4 5
#             Enter value of K: 2
#             Rotated list: [3, 4, 5, 1, 2]