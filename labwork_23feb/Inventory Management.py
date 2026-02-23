# Inventory Management

stock = [0, 5, 20, 8, 15, 0, 3]

# Remove items with 0 stock
stock = [s for s in stock if s > 0]

# Add restock
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

total_inventory = sum(stock)

print("Updated Stock:", stock)
print("Total Inventory:", total_inventory)