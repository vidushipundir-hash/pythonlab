
# Taking input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
d = float(input("Enter fourth number: "))

# Assume first number is greatest
greatest = a

# Compare with other numbers
if b > greatest:
    greatest = b

if c > greatest:
    greatest = c

if d > greatest:
    greatest = d

# Print result
print("The greatest number is:", greatest)


#------------------******-------------------******------------------

        #input:
               #Enter first number: 60.2
               #Enter second number: 60.3
               #Enter third number: 50.3
               #Enter fourth number: 50.2

        #output:      
                #The greatest number is: 60.3

#------------------******-------------------******------------------                
