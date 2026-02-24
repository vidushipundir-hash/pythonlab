# -------------------------------------------------
# Program Name : Count Vowels using Function
# -------------------------------------------------

# Function to count vowels
def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count

# Taking input
string = input("Enter a string: ")

# Calling function
result = count_vowels(string)

print("Number of vowels:", result)


#  output:
#     Enter a string: Hello World
#     Number of vowels: 3