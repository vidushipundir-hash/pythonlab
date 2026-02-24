# Problem 89: Find frequency of each character

# Taking input
string = input("Enter a string: ")

# Creating empty dictionary
freq = {}

# Counting frequency
for ch in string:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Printing result
print("Character Frequency:", freq)


#   output:
#        Enter a string: hello
#        Character Frequency: {'h': 1, 'e': 1, 'l': 2, 'o': 1}