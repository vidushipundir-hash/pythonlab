# Problem 1: Swap two numbers without using third variable

# Taking input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swapping without third variable
a = a + b
b = a - b
a = a - b

# Printing result
print("After swapping:")
print("First number =", a)
print("Second number =", b)


#------------------******-------------------******------------------

        #input:
               #Enter first number: 4
               #Enter second number: 8

        #output:
               #After swapping:
               #First number = 8
               #Second number = 4

#------------------******-------------------******------------------               