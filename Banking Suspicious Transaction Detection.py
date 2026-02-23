amount = 250000
account_age = 4   # months
international = True

if amount > 200000 and account_age < 6 and international:
    print("Transaction Flagged for Manual Verification")
else:
    print("Transaction is Normal")