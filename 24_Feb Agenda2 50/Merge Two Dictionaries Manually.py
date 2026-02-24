# -------------------------------------------------
# Program Name : Merge Two Dictionaries
# -------------------------------------------------

n1 = int(input("Enter number of elements in first dictionary: "))
dict1 = {}

for i in range(n1):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

n2 = int(input("Enter number of elements in second dictionary: "))
dict2 = {}

for i in range(n2):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dict2[key] = value

# Merging manually
merged = {}

for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    merged[key] = dict2[key]

print("Merged dictionary:", merged)


#    output:
#           Merged dictionary: {'a': 10, 'b': 20, 'c': 30}