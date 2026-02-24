# -------------------------------------------------
# Program Name : Sort Dictionary by Keys
# -------------------------------------------------

n = int(input("Enter number of elements: "))
data = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

# Sorting by keys
for key in sorted(data.keys()):
    print(key, ":", data[key])


#   output:
#         a : 10
#         b : 20
#         c : 30