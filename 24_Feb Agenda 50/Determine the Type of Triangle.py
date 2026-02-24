
# Taking input from user
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Check if valid triangle
if a + b > c and a + c > b and b + c > a:

    if a == b and b == c:
        print("Equilateral Triangle")

    elif a == b or b == c or a == c:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

else:
    print("Not a valid Triangle")


#----------------------******----------------******--------------------

#          input:
#                 Enter side 1: 8
#                 Enter side 2: 5
#                 Enter side 3: 9

#          output:
#                  Scalene Triangle

#----------------------******----------------******--------------------

