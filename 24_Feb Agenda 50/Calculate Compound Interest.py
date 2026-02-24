
# Taking input
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time (in years): "))

# Calculating compound interest
amount = p * (1 + r/100) ** t
ci = amount - p

# Printing result
print("Compound Interest =", ci)