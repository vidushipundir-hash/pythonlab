# -------------------------------------------------
# Program Name : Unique Elements using Function
# -------------------------------------------------

# Function to return unique elements
def unique_elements(lst):
    unique_list = []
    
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

# Taking input (space separated numbers)
numbers = list(map(int, input("Enter elements: ").split()))

# Calling function
result = unique_elements(numbers)

print("Unique elements:", result)


# output:
#    Enter elements: 1 2 2 3 4 4 5
#    Unique elements: [1, 2, 3, 4, 5]