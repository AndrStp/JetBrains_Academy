from random import choice


def main():
    user_num = int(input('Enter the number of friends joining (including you):\n'))
    if user_num < 1:
        print('\nNo one is joining for the party')
    else:
        print('\nEnter the name of every friend (including you), each on a new line:')
        users = {}
        for _ in range(user_num):
            user = input()
            users[user] = 0

        print()
        bill = int(input('Enter the total bill value:\n'))
        decision = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').lower()
        if decision == 'yes':
            lucky = lucky_split(users)
            guests = split_bill_lucky(bill, users, lucky)
            print(f'\n{lucky} is the lucky one!\n')
            print(guests)
        else:
            users = split_bill(bill, users)
            print('\nNo one is going to be lucky\n')
            print(users)


def split_bill(bill: int, guests: dict) -> dict:
    """Splits the bill equally among the guests"""
    value = round(bill / len(guests), 2)
    guests = {key: value for key in guests}
    return guests


def split_bill_lucky(bill: int, guests: dict, lucky: str) -> dict:
    """Splits the bill equally among the guests excluding the lucky one"""
    value = round(bill / (len(guests) - 1), 2)
    for guest in guests:
        if guest == lucky:
            guests[guest] = 0
        else:
            guests[guest] = value
    return guests


def lucky_split(guests: dict) -> str:
    """Return random person from the dict of guests"""
    lucky = choice(list(guests.keys()))
    return lucky


if __name__ == '__main__':
    main()
