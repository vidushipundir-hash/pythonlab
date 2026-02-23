# Program 3: Contact Book using Dictionary

# Dictionary storing name and phone number
contacts = {
    "Ravi": "9876543210",
    "Simran": "9123456780",
    "Aman": "9988776655"
}

# Display contacts
print("Contact List:")
for name, number in contacts.items():
    print(name, ":", number)

# Search contact
search_name = "Ravi"
if search_name in contacts:
    print("Phone Number of", search_name, "is:", contacts[search_name])
else:
    print("Contact not found")