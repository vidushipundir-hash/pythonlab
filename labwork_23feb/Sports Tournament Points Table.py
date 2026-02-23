# Sports Tournament Points Table

points = [45, 60, -10, 30, 75, 50]

# Replace negative points with 0
for i in range(len(points)):
    if points[i] < 0:
        points[i] = 0

points.sort(reverse=True)

winner = points[0]
runner_up = points[1]

print("Leaderboard:", points)
print("Winner Points:", winner)
print("Runner-up Points:", runner_up)