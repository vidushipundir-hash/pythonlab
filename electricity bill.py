units = 350
senior_citizen = True

# Bill calculation
if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

# Senior citizen discount
if senior_citizen:
    bill = bill - (bill * 0.10)

print("Total Electricity Bill =", bill)