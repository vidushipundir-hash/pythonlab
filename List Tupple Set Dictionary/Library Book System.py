# Program 7: Library System

# List of borrowed books
borrowed_books = ["Python", "Math", "Python", "Science"]

# Tuple of available books
available_books = ("Python", "Math", "Science", "English")

# Set of unique borrowed books
unique_borrowed = set(borrowed_books)

# Dictionary to count borrow frequency
borrow_count = {}

for book in borrowed_books:
    borrow_count[book] = borrow_count.get(book, 0) + 1

print("Available Books:", available_books)
print("Unique Borrowed:", unique_borrowed)
print("Borrow Count:", borrow_count)