num = input("Enter a number or string: ")

if num == num[::-1]:
    print("It is a Palindrome")
else:
    print("It is Not a Palindrome")