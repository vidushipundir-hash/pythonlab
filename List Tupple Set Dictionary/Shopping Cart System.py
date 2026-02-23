# Program 5: Shopping Cart

# List of items
cart = ["Apple", "Banana", "Milk", "Apple"]

# Tuple of fixed prices
prices = (50, 30, 40)

# Set of unique items
unique_items = set(cart)

# Dictionary for item count
item_count = {}

for item in cart:
    item_count[item] = item_count.get(item, 0) + 1

print("Unique Items:", unique_items)
print("Item Count:", item_count)