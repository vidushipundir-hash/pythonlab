credit_score = 720
income = 40000
existing_loan = 2000

if credit_score < 600:
    print("Loan Rejected: Low Credit Score")
elif 600 <= credit_score < 750:
    if income < 30000:
        print("Loan Rejected: Income too low")
    elif income < 30000 and existing_loan > 5000:
        print("Loan Rejected")
    else:
        print("Further Income Check Required")
else:
    if income < 30000 and existing_loan > 5000:
        print("Loan Rejected")
    else:
        print("Loan Approved")