# Program 10: Inventory System

# List of products sold
sold_products = ["Pen", "Pencil", "Pen", "Eraser"]

# Tuple of all products
all_products = ("Pen", "Pencil", "Eraser", "Scale")

# Set of unique sold products
unique_sold = set(sold_products)

# Dictionary to track stock
stock = {
    "Pen": 100,
    "Pencil": 150,
    "Eraser": 80,
    "Scale": 50
}

# Reduce stock for sold items
for product in sold_products:
    stock[product] -= 1

print("Unique Sold Products:", unique_sold)
print("Updated Stock:", stock)