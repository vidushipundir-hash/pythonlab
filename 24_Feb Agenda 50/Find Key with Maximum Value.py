# -------------------------------------------------
# Program Name : Find Key with Maximum Value
# -------------------------------------------------

n = int(input("Enter number of elements: "))
data = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

# Finding maximum value key
max_key = max(data, key=data.get)

print("Key with maximum value:", max_key)
print("Maximum value:", data[max_key])


#    output:
#          Key with maximum value: Ravi
#          Maximum value: 95