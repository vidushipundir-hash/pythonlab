# -----------------------------------------------
# Program Name : Star Pattern
# Description  : Prints a right-angle triangle pattern
# -----------------------------------------------

# Taking input
n = int(input("Enter number of rows: "))

# Outer loop for rows
for i in range(1, n + 1):
    
    # Inner loop for printing stars
    for j in range(i):
        print("*", end=" ")
    
    print()   # Move to next line

#   Enter number of rows: 5
#    *
#    * *
#    * * *
#    * * * *
#    * * * * *