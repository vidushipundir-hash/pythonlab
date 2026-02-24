
# Taking input from user
ch = input("Enter a character: ")

# Check if single character
if len(ch) == 1:

    if ch.isdigit():
        print("It is a Digit")

    elif ch.isalpha():
        print("It is an Alphabet")

    else:
        print("It is a Special Character")

else:
    print("Invalid Input")


#-----------------******----------------******--------------------

        #input:
              #Enter a character: *

        #output:      
              #It is a Special Character
              
#-----------------******----------------******--------------------
