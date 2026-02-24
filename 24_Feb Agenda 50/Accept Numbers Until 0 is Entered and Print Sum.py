# Program to accept numbers until 0 and print sum

total = 0

num = int(input("Enter number (0 to stop): "))

while num != 0:
    total = total + num
    num = int(input("Enter number (0 to stop): "))

print("Sum is:", total)

#     output:
#     Enter number (0 to stop): 5
#     Enter number (0 to stop): 3
#     Enter number (0 to stop): 2
#     Enter number (0 to stop): 0
#     Sum is: 10