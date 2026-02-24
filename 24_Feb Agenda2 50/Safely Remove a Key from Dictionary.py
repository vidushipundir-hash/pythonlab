# -------------------------------------------------
# Program Name : Safely Remove Key from Dictionary
# -------------------------------------------------

n = int(input("Enter number of elements: "))
data = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

remove_key = input("Enter key to remove: ")

# Safe removal
if remove_key in data:
    del data[remove_key]
    print("Key removed successfully.")
else:
    print("Key not found.")

print("Updated dictionary:", data)


#     output:
#           Enter key to remove: a
#           Key removed successfully.
#           Updated dictionary: {'b': 20, 'c': 30}