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
            successful = bank.Bank.log_in(bankie)
            if not successful:
                print('\nWrong card number or PIN!\n')
            else:
                print('\nYou have successfully logged in!\n')
                while True:
                    display_menu(bankie)
                    option = input()
                    if option == '1':
                        display_balance(bankie)
                        continue
                    if option == '2':
                        bank.Bank.log_out(bankie)
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
            '2. Log out\n'
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
