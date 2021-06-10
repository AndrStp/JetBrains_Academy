import bank, client
import sqlite3


def main():
    """Runs the bank :)"""
    bankie = bank.Bank()  # creates a bank
    connect_db()  # connecting (creating) a database 'card'
    while True:
        global flag
        flag = False
        display_menu(bankie)
        choice = input()
        if choice == '0':
            break
        if choice == '1':
            create_client(bankie)
            continue
        elif choice == '2':
            print()
            successful = bankie.log_in()
            if not successful:
                print('\nWrong card number or PIN!\n')
            else:
                print('\nYou have successfully logged in!\n')
                while True:
                    display_menu(bankie)
                    option = input()
                    if option == '1':
                        display_balance(bankie)
                    if option == '2':
                        income = int(input('\nEnter income:\n'))
                        bankie.add_income(income)
                        print('Income was added!\n')
                    if option == '3':
                        print('\nTransfer')
                        account = input('Enter card number:\n')
                        valid_account = client.Client.is_valid_num(bankie.client, account)
                        if not valid_account:
                            print('Probably you made a mistake in the card number. Please try again!\n')
                            continue
                        if not bankie.in_db(account):
                            print('Such a card does not exist.\n')
                            continue
                        amount = int(input('Enter how much money you want to transfer:\n'))
                        if not bankie.check_balance(amount):
                            print('Not enough money!\n')
                            continue
                        bankie.transfer(account, amount)
                        print('Success!\n')
                    if option == '4':
                        bankie.close_acc()
                        bankie.log_out()
                        print('\nThe account has been closed!\n')
                        break
                    if option == '5':
                        bankie.log_out()
                        print('\nYou have successfully logged out!\n')
                        break
                    if option == '0':
                        flag = True
                        break
            if flag:
                break

    print('\nBye!')


def connect_db():
    """Creates (connects) to the db"""
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS card (
                id INTEGER,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0
                )""")
    conn.commit()
    conn.close()


def display_menu(fin: bank.Bank):
    """Displays the menu"""
    if fin.client_logged:
        print(
            '1. Balance\n'
            '2. Add income\n'
            '3. Do transfer\n'
            '4. Close account\n'
            '5. Log out\n'
            '0. Exit'
        )
    else:
        print(
            '1. Create an account\n'
            '2. Log into account\n'
            '0. Exit'
        )


def display_balance(fin: bank.Bank):
    """Displays the balance for the current client"""
    balance = bank.Bank.balance(fin)
    print(f'\nBalance: {balance}\n')


def create_client(fin: bank.Bank):
    """Create a card (client)"""
    user = client.Client()
    fin.update_db(user)
    print('\nYour card has been created')
    print('Your card number:')
    print(user.card_number)
    print('Your card PIN:')
    print(user.pin)
    print()


if __name__ == '__main__':
    main()
