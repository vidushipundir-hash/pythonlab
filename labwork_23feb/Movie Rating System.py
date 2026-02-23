# Movie Rating System

ratings = [5, 4, 3, 6, 2, 5, 1, 0]

# Remove invalid ratings
valid_ratings = []
for r in ratings:
    if 1 <= r <= 5:
        valid_ratings.append(r)

average = sum(valid_ratings) / len(valid_ratings)

five_star = valid_ratings.count(5)

valid_ratings.sort()

print("Valid Ratings:", valid_ratings)
print("Average Rating:", average)
print("5-Star Ratings:", five_star)