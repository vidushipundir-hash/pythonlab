# -------------------------------------------------
# Program Name : Calculate Power without **
# -------------------------------------------------

base = int(input("Enter base number: "))
exp = int(input("Enter exponent: "))

result = 1

# Multiply base exp times
for i in range(exp):
    result = result * base

print(base, "raised to", exp, "is:", result)

#  output:
# Enter base number: 2
# Enter exponent: 5
# 2 raised to 5 is: 32
