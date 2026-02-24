# Problem 92: Find longest word in a sentence

# Taking input
sentence = input("Enter a sentence: ")

words = sentence.split()

longest = words[0]

# Finding longest word
for word in words:
    if len(word) > len(longest):
        longest = word

# Printing result
print("Longest word:", longest)

#    output:
#           Enter a sentence: Python programming language
#           Longest word: programming