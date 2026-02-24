# Program to generate Fibonacci series

n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 1

while count <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1


 #     Output:
 #             Enter number of terms: 7
 #             0 1 1 2 3 5 8
 
  
     