# Shopping Bill Calculation

# Prices and quantities
notebooks = 3
price_notebook = 45

pens = 2
price_pen = 20

# Calculate total cost
total_notebooks = notebooks * price_notebook
total_pens = pens * price_pen

total_bill = total_notebooks + total_pens

# Customer payment
payment = 500
balance = payment - total_bill

# Display results
print("Total bill amount =", total_bill)
print("Remaining balance =", balance)