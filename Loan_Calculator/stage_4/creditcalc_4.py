import math
import sys
import argparse


def main():
    option, interest, loan_principal, periods, payment = take_args()
    correct = check_args(option, interest, loan_principal, periods, payment)
    if not correct:
        print('Incorrect parameters')
        return
    if option == 'diff':
        pays = calc_diff(loan_principal, periods, interest)
        overpay = calc_overpay(loan_principal, diff=pays)
        display_diff(pays)
        print(f'\nOverpayment = {overpay}')
    if option == 'annuity':
        if not loan_principal:
            principal = calc_principal(payment, periods, interest)
            overpay = calc_overpay(principal, ann=payment, periods=periods)
            print(f'Your loan principal = {principal}!')
            print(f'Overpayment = {overpay}')
        if not payment:
            pay = calc_payment(loan_principal, periods, interest)
            overpay = calc_overpay(loan_principal, ann=pay, periods=periods)
            print(f'Your annuity payment = {pay}!')
            print(f'Overpayment = {overpay}')
        if not periods:
            months = calc_periods(loan_principal, payment, interest)
            overpay = calc_overpay(loan_principal, ann=payment, periods=months)
            display_periods(months)
            print(f'Overpayment = {overpay}')


def take_args():
    parser = argparse.ArgumentParser(description='Calculate the differentiate payment or annuity payment', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--type', choices=['diff', 'annuity'], help="pass 'diff' to calculate differentiate payment\n"
                                                                    "pass 'annuity' to calculate annuity payment")
    parser.add_argument('--interest', type=float, help='pass the interest rate')
    parser.add_argument('--principal', type=int, help='pass the loan principal')
    parser.add_argument('--periods', type=int, help='pass the the number of months needed to repay the loan')
    parser.add_argument('--payment', type=int, help='pass the monthly payment amount')

    args = parser.parse_args()
    option = args.type
    interest = args.interest
    loan_principal = args.principal
    periods = args.periods
    payment = args.payment

    return option, interest, loan_principal, periods, payment


def check_args(option, interest, loan_principal, periods, payment):
    """Returns whether the parameters provided are valid"""
    # check the length of the parameters
    parameters = sys.argv[1:]
    if len(parameters) != 4:
        return False
    # check if the option parameter is passed
    if not option:
        return False
    # check if the numerical parameters are positive
    nums = [interest, loan_principal, periods]
    for num in nums:
        if num and num < 0:
            return False
    # checks if all necessary parameters are provided for 'diff' option
    if option == 'diff':
        args = [option, interest, loan_principal, periods]
        if payment:
            return False
        elif not all(args):
            return False
    return True


def calc_periods(loan_principal, payment, interest):
    """Returns how many periods are needed to repay a debt"""
    nominal = interest / 100 / 12
    periods = math.log((payment / (payment - nominal * loan_principal)), 1 + nominal)
    return math.ceil(periods)


def calc_payment(loan_principal, periods, interest):
    """Returns the annuity period payments"""
    nominal = interest / 100 / 12
    payment = loan_principal * (nominal * pow(1 + nominal, periods)) / (pow(1 + nominal, periods) - 1)
    return math.ceil(payment)


def calc_principal(payment, periods, interest):
    """Returns the loan principal"""
    nominal = interest / 100 / 12
    principal = payment / ((nominal * pow(1 + nominal, periods)) / (pow(1 + nominal, periods) - 1))
    return math.ceil(principal)


def calc_overpay(loan_principal, diff=None, ann=None, periods=None):
    """Returns how much you are going to overpay"""
    if diff is None:
        overpay = abs(loan_principal - ann * periods)
        return overpay
    else:
        overpay = abs(loan_principal - sum((payment for payment in diff)))
        return overpay


def calc_diff(loan_principal, periods, interest) -> list:
    """Returns monthly diff payments"""
    nominal = interest / 100 / 12
    diff_pays = []
    for month in range(1, periods+1):
        pay = loan_principal / periods + nominal * (loan_principal - (loan_principal * (month - 1)) / periods)
        diff_pays.append(math.ceil(pay))
    return diff_pays


def display_diff(payments: list):
    """Displays the diff payments in a fancy way"""
    for i, payment in enumerate(payments, 1):
        print(f'Month {i}: payment is {payment}')


def display_periods(periods):
    """Displays the payments to repay debt in a fancy way"""
    if periods < 12:
        print(f'It will take {periods} months to repay this loan!')
    else:
        if periods % 12 == 0:
            print(f'It will take {periods // 12} years to repay this loan!')
        else:
            print(f'It will take {periods // 12} years and {periods % 12} months to repay this loan!')


if __name__ == '__main__':
    main()
