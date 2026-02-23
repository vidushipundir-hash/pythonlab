# Program 3: Word Frequency Counter

sentence = "python is easy and python is powerful"

# Convert sentence into list
words_list = sentence.split()

# Tuple of words
words_tuple = tuple(words_list)

# Set of unique words
unique_words = set(words_list)

# Dictionary for frequency
frequency = {}

for word in words_list:
    frequency[word] = frequency.get(word, 0) + 1

print("Words Tuple:", words_tuple)
print("Unique Words:", unique_words)
print("Word Frequency:", frequency)