# E-Commerce Cart System

cart = [2000, 1500, 2000, 3000, 800]

# Remove duplicate items
cart = list(set(cart))
print("Unique Items:", cart)

total = sum(cart)
print("Total Amount:", total)

# Apply discount
if total > 5000:
    discount = total * 0.10
    total -= discount
    print("Discount Applied:", discount)

# Add GST 18%
gst = total * 0.18
final_amount = total + gst

print("GST Added:", gst)
print("Final Payable Amount:", final_amount)