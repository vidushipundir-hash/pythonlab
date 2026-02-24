# -------------------------------------------------
# Program Name : Check Key in Dictionary
# -------------------------------------------------

n = int(input("Enter number of elements: "))
data = {}

# Taking dictionary input
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

check_key = input("Enter key to check: ")

# Checking key existence
if check_key in data:
    print("Key exists in dictionary")
else:
    print("Key does not exist in dictionary")


#    output:
#         Enter number of elements: 2
#          Enter key: a
#          Enter value: 10
#          Enter key: b
#          Enter value: 20
#          Enter key to check: a
#          Key exists in dictionary