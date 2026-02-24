# Problem 88: Count number of words in a sentence

# Taking input from user
sentence = input("Enter a sentence: ")

# Splitting sentence into words
words = sentence.split()

# Counting words
count = len(words)

# Printing result
print("Number of words:", count)

#   output:
#         Enter a sentence: Python is very easy to learn
#         Number of words: 6