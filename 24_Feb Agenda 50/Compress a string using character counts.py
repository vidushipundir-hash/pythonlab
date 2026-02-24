# Problem 100: Compress a string using character counts

# Taking input
string = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i + 1]:
        count += 1
    else:
        compressed += string[i] + str(count)
        count = 1

# Printing result
print("Compressed string:", compressed)


#   output:
#       Enter a string: aaabbc
#       Compressed string: a3b2c1