l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

lsa = 2 * h * (l + b)
tsa = 2 * (l*b + b*h + l*h)
volume = l * b * h

print("Curved Surface Area (LSA) =", lsa)
print("Total Surface Area =", tsa)
print("Volume =", volume)