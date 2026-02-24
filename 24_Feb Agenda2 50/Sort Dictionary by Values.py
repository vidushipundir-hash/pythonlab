# -------------------------------------------------
# Program Name : Sort Dictionary by Values
# -------------------------------------------------

n = int(input("Enter number of elements: "))
data = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

# Sorting by values
sorted_items = sorted(data.items(), key=lambda item: item[1])

for key, value in sorted_items:
    print(key, ":", value)



#    output:
#          b : 10
#          a : 20
#          c : 30