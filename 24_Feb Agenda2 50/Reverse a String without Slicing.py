# -------------------------------------------------
# Program Name : Reverse String without Slicing
# -------------------------------------------------

text = input("Enter a string: ")

reverse = ""

# Using loop to reverse string
for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)


#    output:
#      Enter a string: Python
#       Reversed string: nohtyP