cart_value = 5000
membership = "Gold"
festival = True

discount = 0

# Membership discount
if membership == "Silver":
    discount = 0.10
elif membership == "Gold":
    discount = 0.20
elif membership == "Platinum":
    discount = 0.30

# Festival extra 5%
if festival:
    discount = max(discount, 0.25)

final_amount = cart_value - (cart_value * discount)

print("Final Payable Amount =", final_amount)