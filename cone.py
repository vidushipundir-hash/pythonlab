import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

l = math.sqrt(r*r + h*h)

csa = math.pi * r * l
tsa = math.pi * r * (r + l)
volume = (1/3) * math.pi * r * r * h

print("Curved Surface Area =", round(csa,2))
print("Total Surface Area =", round(tsa,2))
print("Volume =", round(volume,2))