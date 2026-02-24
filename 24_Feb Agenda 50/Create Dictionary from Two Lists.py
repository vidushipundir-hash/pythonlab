# -------------------------------------------------
# Program Name : Create Dictionary from Two Lists
# -------------------------------------------------

keys = input("Enter keys (space separated): ").split()
values = list(map(int, input("Enter values (space separated): ").split()))

# Creating dictionary
data = {}

for i in range(len(keys)):
    data[keys[i]] = values[i]

print("Created dictionary:", data)

#   output:
#         Enter keys (space separated): a b c
#         Enter values (space separated): 10 20 30
#         Created dictionary: {'a': 10, 'b': 20, 'c': 30}