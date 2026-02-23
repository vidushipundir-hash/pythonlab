balance = 60000
withdraw_amount = 30000
atm_cash = 50000

if withdraw_amount > balance:
    print("Transaction Failed: Insufficient Balance")
elif withdraw_amount > 50000:
    print("Transaction Failed: Exceeds Daily Limit")
elif withdraw_amount > atm_cash:
    print("Transaction Failed: ATM Out of Cash")
else:
    balance -= withdraw_amount
    atm_cash -= withdraw_amount
    print("Withdrawal Successful")
    print("Remaining Balance =", balance)