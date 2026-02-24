# -------------------------------------------------
# Program Name : Reverse List without reverse()
# -------------------------------------------------

numbers = list(map(int, input("Enter elements: ").split()))

reversed_list = []

# Loop from last index to first
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list:", reversed_list)



#      output:
#            Enter elements: 1 2 3 4 5
#            Reversed list: [5, 4, 3, 2, 1]