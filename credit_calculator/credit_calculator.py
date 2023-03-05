import math

language = input("Choose language (en,ua): ")
if language == "en":
    # English translations
    welcome_message = "Welcome \n" \
                      " Power by Stell!"
    calculation_options = "What do you want to calculate?\n" \
                          "type 'n' for number of monthly payments,\n" \
                          "type 'a' for annuity monthly payment amount,\n" \
                          "type 'p' for loan principal,\n" \
                          "type 'd' for differentiated payment."
    principal_prompt = "Enter the loan principal:"
    num_periods = "Enter the number of periods:"
    periods_prompt = "Enter the number of periods:"
    payment_prompt = "Enter the monthly payment:"
    interest_prompt = "Enter the loan interest:"
    payment_result = "Your monthly payment = "
    periods_result = "It will take "
    overpayment_result = "Overpayment = {} "
    year_prompt = "It will take {} months to repay this loan!"
    mount_prompt = "It will take {} years to repay this loan!"
    m_y_prompt = "It will take {} years and {} months to repay this loan!"
    periods_numb = "Enter the number of periods:"
    periods_m_y = "You need to pay {} per month for {} months"
    periods_m_and_y = "You need to pay {} per month for {} years and {} months"
    l_principal = "Your loan principal = {} with {} months to repay"
    principal_m_y = "Your loan principal = {} with {} years and {} months to repay"
    mount_pay = "Month {}: payment is {}"
    Error = "Invalid calculation type"
    Error2 = "Invalid language choice."

elif language == "ua":
    # Ukrainian translations
    welcome_message = "Вітаю \n" \
                      "Power by Stell!"
    calculation_options = "Що ви хочете обчислити?\n" \
                          "введіть 'n' для кількості щомісячних платежів,\n" \
                          "введіть 'a' для суми щомісячного платежу,\n" \
                          "введіть 'p' для суми кредиту,\n" \
                          "введіть 'd' для диференціальних платежів."
    principal_prompt = "Введіть суму кредиту:"
    num_periods = "Введіть кількість періодів:"
    periods_prompt = "Введіть кількість періодів:"
    payment_prompt = "Введіть щомісячний платіж:"
    interest_prompt = "Введіть відсотки по кредиту:"
    payment_result = "Ваш щомісячний платіж = "
    periods_result = "Кредит буде виплачено "
    overpayment_result = "переплата = {}"
    year_prompt = "На погашення цієї позики знадобиться {} місяців!"
    mount_prompt = "На погашення цієї позики знадобиться {} років!"
    m_y_prompt = "На погашення цієї позики знадобиться {} років і {} місяців!"
    periods_numb =" Введіть кількість періодів:"
    periods_m_y = "Вам потрібно платити {} на місяць протягом {} місяців "
    periods_m_and_y = "Вам потрібно платити {} на місяць протягом {} років і {} місяців"
    l_principal = "Основна сума вашої позики = {} із {} місяців до погашення"
    principal_m_y = "Основна сума вашої позики = {} з {} років і {} місяців до погашення"
    mount_pay = "Місяць {}: платіж становить {}"
    Error = "Недійсний тип обчислення"
    Error2 = "Недійсний вибір мови."

else:
    print(Error2)

print(welcome_message)
print(calculation_options)

calculation_type = input()
if calculation_type == 'n':
    print(principal_prompt)
    loan_principal = float(input())
    print(payment_prompt)
    monthly_payment = float(input())
    print(interest_prompt)
    interest = float(input()) / 1200

    n = math.ceil(math.log(monthly_payment / (monthly_payment - interest * loan_principal), 1 + interest))
    if n > 0:
        years, months = divmod(n, 12)
        if years == 0:
            print(year_prompt.format(months))
        elif months == 0:
            print(mount_prompt.format(years))
        else:
            print(m_y_prompt.format(years, months))
    else:
        print("The loan cannot be repaid with this monthly payment!")

elif calculation_type == 'a':
    print(principal_prompt)
    loan_principal = float(input())
    print(periods_prompt)
    n = int(input())
    print(interest_prompt)
    interest = float(input()) / 1200

    annuity_payment = loan_principal * (interest * (1 + interest)**n) / ((1 + interest)**n - 1)

    years, months = divmod(n, 12)
    if years == 0:
        print(periods_m_y.format(round(annuity_payment), months))
    elif months == 0:
        print(periods_m_y.format(round(annuity_payment), years))
    else:
        print(periods_m_and_y.format(round(annuity_payment), years, months))

elif calculation_type == 'p':
    print(payment_prompt)
    annuity_payment = float(input())
    print(periods_numb)
    n = int(input())
    print(interest_prompt )
    interest = float(input()) / 1200

    loan_principal = annuity_payment / ((interest * (1 + interest)**n) / ((1 + interest)**n - 1))

    years, months = divmod(n, 12)
    if years == 0:
        print(l_principal.format(round(loan_principal), months))
    elif months == 0:
        print(l_principal.format(round(loan_principal), years))
    else:
        print(principal_m_y.format(round(loan_principal), years, months))

elif calculation_type == 'd':
    print(principal_prompt)
    loan_principal = float(input())
    print(num_periods)
    n = int(input())
    print(interest_prompt)
    interest = float(input()) / 1200

    total_payment = 0

    for month in range(1,n +1):
        differentiated_payment = loan_principal / n + interest * (loan_principal - loan_principal * (month - 1) / n)
        total_payment += differentiated_payment
        print(mount_pay.format(month, math.ceil(differentiated_payment)))

        overpayment = total_payment - loan_principal
        print(overpayment_result.format(round(overpayment)))

else:
    print(Error)
