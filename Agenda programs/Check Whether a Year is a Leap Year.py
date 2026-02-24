
# Taking input from user
year = int(input("Enter a year: "))

# Checking leap year condition
if (year % 400 == 0):
    print("It is a Leap Year")

elif (year % 100 == 0):
    print("It is NOT a Leap Year")

elif (year % 4 == 0):
    print("It is a Leap Year")

else:
    print("It is NOT a Leap Year")


#----------------------******----------------******--------------------

#         input:
#                Enter a year: 2017

#         output:
#                It is NOT a Leap Year

#----------------------******----------------******--------------------