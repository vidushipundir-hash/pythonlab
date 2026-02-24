# -----------------------------------------------
# Program Name : Count Vowels in String
# -----------------------------------------------

text = input("Enter a string: ")
count = 0

for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels:", count)

#  output:
#  Enter a string: Hello World
#  Number of vowels: 3