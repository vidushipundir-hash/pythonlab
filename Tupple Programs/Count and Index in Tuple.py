# -------------------------------------------------
# Program Name : Count and Index in Tuple
# Description  : This program counts occurrences
#                and finds index of an element.
# -------------------------------------------------

# Creating tuple
data = (1, 2, 3, 2, 4, 2, 5)

# Counting occurrence of 2
count_value = data.count(2)

# Finding index of first 4
index_value = data.index(4)

# Displaying result
print("Count of 2 :", count_value)
print("Index of 4 :", index_value)