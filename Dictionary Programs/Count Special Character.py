# Program to count special characters in a sentence

sentence = input("Enter a sentence: ")

count = 0

for ch in sentence:
    # Check if character is NOT alphabet and NOT digit and NOT space
    if not ch.isalnum():
        count += 1

print("Number of special characters:", count)