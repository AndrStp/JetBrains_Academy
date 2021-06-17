import math


def main():
    print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
    option = input()
    if option == 'n':
        loan_principal, payment, interest = read('n')
        periods = calc_periods(loan_principal, payment, interest)
        display_periods(periods)
    elif option == 'a':
        loan_principal, periods, interest = read('a')
        payment = calc_payment(loan_principal, periods, interest)
        print(f'Your monthly payment = {payment}!')
    else:
        payment, periods, interest = read('p')
        loan_principal = calc_principal(payment, periods, interest)
        print(f'Your loan principal = {loan_principal}!')


def read(option):
    if option == 'n':
        loan_principal = float(input('Enter the loan principal:\n'))
        payment = int(input('Enter the monthly payment:\n'))
        interest = float(input('Enter the loan interest:\n'))
        return loan_principal, payment, interest / 100
    elif option == 'a':
        loan_principal = float(input('Enter the loan principal:\n'))
        periods = int(input('Enter the number of periods payment:\n'))
        interest = float(input('Enter the loan interest:\n'))
        return loan_principal, periods, interest / 100
    elif option == 'p':
        payment = float(input('Enter the loan principal:\n'))
        periods = int(input('Enter the number of periods payment:\n'))
        interest = float(input('Enter the loan interest:\n'))
        return payment, periods, interest / 100


def calc_periods(loan_principal, payment, interest):
    nominal_interest = interest / 12
    periods = math.log((payment / (payment - nominal_interest * loan_principal)), 1 + nominal_interest)
    return math.ceil(periods)


def calc_payment(loan_principal, periods, interest):
    nominal_interest = interest / 12
    payment = loan_principal * (nominal_interest * pow(1 + nominal_interest, periods)) / (pow(1 + nominal_interest, periods) - 1)
    return math.ceil(payment)


def calc_principal(payment, periods, interest):
    nominal_interest = interest / 12
    principal = payment / ((nominal_interest * pow(1 + nominal_interest, periods)) / (pow(1 + nominal_interest, periods) - 1))
    return principal


def display_periods(periods):
    if periods < 12:
        print(f'It will take {periods} months to repay this loan!')
    else:
        if periods % 12 == 0:
            print(f'It will take {periods // 12} years to repay this loan!')
        else:
            print(f'It will take {periods // 12} years and {periods % 12} months to repay this loan!')


if __name__ == '__main__':
    main()
