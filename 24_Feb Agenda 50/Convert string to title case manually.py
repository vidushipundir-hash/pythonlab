# Problem 91: Convert string to title case manually

# Taking input
sentence = input("Enter a sentence: ")

words = sentence.split()
title_sentence = ""

# Converting manually
for word in words:
    title_word = word[0].upper() + word[1:].lower()
    title_sentence += title_word + " "

# Printing result
print("Title Case:", title_sentence.strip())

#    output:
#         Enter a sentence: python is FUN
#         Title Case: Python Is Fun