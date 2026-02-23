# Salary Processing System

salaries = [25000, 60000, 45000, 80000, 15000, 52000]

# Remove salaries below minimum wage (20000)
valid_salaries = []
for s in salaries:
    if s >= 20000:
        valid_salaries.append(s)

# Add 5% bonus
for i in range(len(valid_salaries)):
    if valid_salaries[i] > 50000:
        valid_salaries[i] += valid_salaries[i] * 0.05

# Sort descending
valid_salaries.sort(reverse=True)

print("Processed Salaries:", valid_salaries)
print("Top 3 Salaries:", valid_salaries[:3])