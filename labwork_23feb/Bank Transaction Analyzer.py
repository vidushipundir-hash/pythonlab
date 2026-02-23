# Bank Transaction Analyzer

transactions = [10000, -5000, 20000, -10000, 15000, -2000]

# Total balance
balance = sum(transactions)
print("Total Balance:", balance)

# Largest withdrawal
withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals)
print("Largest Withdrawal:", largest_withdrawal)

# Deposits greater than 10000
count = 0
for t in transactions:
    if t > 10000:
        count += 1

print("Deposits > 10000:", count)