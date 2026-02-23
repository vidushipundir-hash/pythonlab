import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

csa = 2 * math.pi * r * h
tsa = 2 * math.pi * r * (r + h)
volume = math.pi * r * r * h

print("Curved Surface Area =", round(csa,2))
print("Total Surface Area =", round(tsa,2))
print("Volume =", round(volume,2))