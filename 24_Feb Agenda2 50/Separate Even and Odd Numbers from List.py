# -------------------------------------------------
# Program Name : Separate Even and Odd Numbers
# -------------------------------------------------

numbers = list(map(int, input("Enter elements: ").split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)


#    output:
#          Enter elements: 1 2 3 4 5 6
#          Even numbers: [2, 4, 6]
#          Odd numbers: [1, 3, 5]