# Program to find GCD of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD is:", a)

#      output:
#             Enter first number: 12
#             Enter second number: 18
#              GCD is: 6
