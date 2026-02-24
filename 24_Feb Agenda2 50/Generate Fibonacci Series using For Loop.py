# -----------------------------------------------
# Program Name : Fibonacci Series (For Loop)
# -----------------------------------------------

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

#  output:
#    Enter number of terms: 7
#    0 1 1 2 3 5 8