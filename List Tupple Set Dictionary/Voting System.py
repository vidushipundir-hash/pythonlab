# Program 6: Voting System

# List of votes
votes = ["A", "B", "A", "C", "B", "A"]

# Tuple of candidates
candidates = ("A", "B", "C")

# Set of candidates who got votes
voted_candidates = set(votes)

# Dictionary to count votes
vote_count = {}

for vote in votes:
    vote_count[vote] = vote_count.get(vote, 0) + 1

print("Candidates:", candidates)
print("Vote Count:", vote_count)