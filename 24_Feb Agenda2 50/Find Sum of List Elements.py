# -------------------------------------------------
# Program Name : Sum of List Elements
# -------------------------------------------------

numbers = list(map(int, input("Enter elements: ").split()))

total = 0

for num in numbers:
    total += num

print("Sum of elements:", total)



#    output:
#           Enter elements: 5 10 15
#           Sum of elements: 30