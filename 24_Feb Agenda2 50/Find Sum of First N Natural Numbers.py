# -----------------------------------------------
# Program Name : Sum of First N Natural Numbers
# -----------------------------------------------

n = int(input("Enter value of N: "))
total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum of first", n, "natural numbers is:", total)


# output:
# Enter value of N: 10
# Sum of first 10 natural numbers is: 55