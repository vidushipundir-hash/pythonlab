
# Taking input from user
ch = input("Enter a character: ")

# Check if input is single alphabet
if len(ch) == 1 and ch.isalpha():

    # Convert to lowercase for easy comparison
    ch = ch.lower()

    # Check vowel condition
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("It is a Vowel")
    else:
        print("It is a Consonant")

else:
    print("Invalid Input")


#-----------------******----------------******--------------------

        #input:
              #Enter a character: p

        #output:
              #It is a Consonant

#-----------------******----------------******--------------------