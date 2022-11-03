def estimator():
    years = int(input("Enter the number of years you will be saving: "))
    principal = float(input("Enter amount of money currently in account: "))
    monthly_invest = float(input("Enter amount you plan on investing monthly: "))
    interest = float(input("Enter interest in decimal numbers (10% = 0.1):" ))

    monthly_invest = monthly_invest *12
    final_amount = 0

    for i in range(0,years):
        if final_amount == 0:
            final_amount = principal
        final_amount = (final_amount + monthly_invest) * (1+ interest)

    print(f"In {years} years you should have £{final_amount} saved in your account")

estimator()