# -------------------------------------------------
# Program Name : Character Frequency Counter
# -------------------------------------------------

# Taking input string
text = input("Enter a string: ")

frequency = {}

# Counting characters
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character frequency:")
for key in frequency:
    print(key, ":", frequency[key])


#   output:
#        Enter a string: hello
#        Character frequency:
#        h : 1
#        e : 1
#        l : 2
#        o : 1