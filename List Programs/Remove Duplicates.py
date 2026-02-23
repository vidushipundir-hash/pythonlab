# -------------------------------------------------
# Program Name : Remove Duplicates from List
# Description  : This program removes duplicate
#                elements from a list.
# -------------------------------------------------

# Creating a list with duplicates
numbers = [1, 2, 3, 2, 4, 5, 1, 6]

# Removing duplicates using set
unique_list = list(set(numbers))

# Display result
print("Original List :", numbers)
print("List after Removing Duplicates :", unique_list)