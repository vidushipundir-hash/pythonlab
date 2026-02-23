# Program 2: Count Frequency of Words

# Taking a sentence
sentence = "python is easy and python is powerful"

# Splitting sentence into words
words = sentence.split()

# Creating empty dictionary
frequency = {}

# Counting words
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Display result
print("Word Frequency:")
for word, count in frequency.items():
    print(word, ":", count)