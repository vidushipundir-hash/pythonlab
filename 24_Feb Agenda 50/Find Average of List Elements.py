# -------------------------------------------------
# Program Name : Average of List Elements
# -------------------------------------------------

numbers = list(map(int, input("Enter elements: ").split()))

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Average of elements:", average)


#   output:
#      Enter elements: 10 20 30
#      Average of elements: 20.0