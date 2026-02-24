# -------------------------------------------------
# Program Name : Check List Palindrome
# -------------------------------------------------

numbers = list(map(int, input("Enter elements: ").split()))

if numbers == numbers[::-1]:
    print("The list is a Palindrome")
else:
    print("The list is not a Palindrome")


#    output:
#              Enter elements: 1 2 3 2 1
#              The list is a Palindrome