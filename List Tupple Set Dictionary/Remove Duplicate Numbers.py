# Program 2: Remove Duplicates

# List of numbers
numbers = [10, 20, 30, 20, 40, 10, 50]

# Tuple (original numbers stored safely)
original_numbers = tuple(numbers)

# Set to remove duplicates
unique_numbers = set(numbers)

# Dictionary to count occurrences
count_dict = {}

for num in numbers:
    count_dict[num] = count_dict.get(num, 0) + 1

print("Original Tuple:", original_numbers)
print("Unique Set:", unique_numbers)
print("Count Dictionary:", count_dict)