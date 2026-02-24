# Program to print prime numbers between 1 and N

n = int(input("Enter value of N: "))

for num in range(2, n + 1):
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")

#     output:
#             Enter value of N: 10
#             2 3 5 7