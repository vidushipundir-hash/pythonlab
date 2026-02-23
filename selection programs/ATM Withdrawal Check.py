# Program 10: ATM Withdrawal Check

balance = 5000
withdraw = 2000

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)
else:
    print("Insufficient Balance")