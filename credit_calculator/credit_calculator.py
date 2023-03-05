import math

print('Power by Stell \n'
      'Hello \n '
      "What do you want to calculate?")
print("type 'n' for number of monthly payments, \n"
      "type 'a' for annuity monthly payment amount,\n"
      "type 'p' for annuity monthly payment amount,\n"
      "type 'd' for differentiated payment")

calculation_type = input()

if calculation_type == 'n':
    print("Enter the loan principal:")
    loan_principal = float(input())
    print("Enter the monthly payment:")
    monthly_payment = float(input())
    print("Enter the loan interest:")
    interest = float(input()) / 1200

    n = math.ceil(math.log(monthly_payment / (monthly_payment - interest * loan_principal), 1 + interest))
    if n > 0:
        years, months = divmod(n, 12)
        if years == 0:
            print("It will take {} months to repay this loan!".format(months))
        elif months == 0:
            print("It will take {} years to repay this loan!".format(years))
        else:
            print("It will take {} years and {} months to repay this loan!".format(years, months))
    else:
        print("The loan cannot be repaid with this monthly payment!")

elif calculation_type == 'a':
    print("Enter the loan principal:")
    loan_principal = float(input())
    print("Enter the number of periods:")
    n = int(input())
    print("Enter the loan interest:")
    interest = float(input()) / 1200

    annuity_payment = loan_principal * (interest * (1 + interest)**n) / ((1 + interest)**n - 1)

    years, months = divmod(n, 12)
    if years == 0:
        print("You need to pay {} per month for {} months".format(round(annuity_payment), months))
    elif months == 0:
        print("You need to pay {} per month for {} years".format(round(annuity_payment), years))
    else:
        print("You need to pay {} per month for {} years and {} months".format(round(annuity_payment), years, months))

elif calculation_type == 'p':
    print("Enter the annuity payment:")
    annuity_payment = float(input())
    print("Enter the number of periods:")
    n = int(input())
    print("Enter the loan interest:")
    interest = float(input()) / 1200

    loan_principal = annuity_payment / ((interest * (1 + interest)**n) / ((1 + interest)**n - 1))

    years, months = divmod(n, 12)
    if years == 0:
        print("Your loan principal = {} with {} months to repay".format(round(loan_principal), months))
    elif months == 0:
        print("Your loan principal = {} with {} years to repay".format(round(loan_principal), years))
    else:
        print("Your loan principal = {} with {} years and {} months to repay"
              .format(round(loan_principal), years, months))

elif calculation_type == 'd':
    print("Enter the loan principal:")
    loan_principal = float(input())
    print("Enter the number of periods:")
    n = int(input())
    print("Enter the loan interest:")
    interest = float(input()) / 1200

    total_payment = 0

    for month in range(1,n +1):
        differentiated_payment = loan_principal / n + interest * (loan_principal - loan_principal * (month - 1) / n)
        total_payment += differentiated_payment
        print("Month {}: payment is {}".format(month, math.ceil(differentiated_payment)))

        overpayment = total_payment - loan_principal
        print("\nOverpayment = {}".format(round(overpayment)))

else:
    print("Invalid calculation type.")
