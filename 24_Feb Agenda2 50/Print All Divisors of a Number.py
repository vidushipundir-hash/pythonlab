# -----------------------------------------------
# Program Name : Print Divisors
# -----------------------------------------------

num = int(input("Enter a number: "))

print("Divisors of", num, "are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")


#       output:
#        Enter a number: 12
#        Divisors of 12 are:
#        1 2 3 4 6 12