# -------------------------------------------------
# Program Name : Reverse a String (For Loop)
# -------------------------------------------------

# Taking input from user
text = input("Enter a string: ")

reverse = ""   # Empty string to store reversed text

# Loop from last index to first index
for i in range(len(text) - 1, -1, -1):
    reverse = reverse + text[i]

# Printing reversed string
print("Reversed string is:", reverse)

#  output:
#         Enter a string: Python
 #        Reversed string is: nohtyP
