# Problem 94: Check whether two strings are anagrams

# Taking input
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Removing spaces and converting to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Checking anagram
if sorted(str1) == sorted(str2):
    print("Strings are Anagrams")
else:
    print("Strings are NOT Anagrams")


#    output:
#          Enter first string: listen
#          Enter second string: silent
#          Strings are Anagrams