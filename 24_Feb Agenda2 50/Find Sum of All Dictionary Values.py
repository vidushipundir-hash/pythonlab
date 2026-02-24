# -------------------------------------------------
# Program Name : Sum of Dictionary Values
# -------------------------------------------------

n = int(input("Enter number of elements: "))
data = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

total = 0

# Calculating sum of values
for value in data.values():
    total += value

print("Sum of all values:", total)


#    output:
#           Enter number of elements: 3
#           Enter key: a
#           Enter value: 10
#           Enter key: b
#           Enter value: 20
#           Enter key: c
#           Enter value: 30
#           Sum of all values: 60