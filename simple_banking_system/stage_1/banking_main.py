import bank, client


def main():
    bankie = bank.Bank()
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


def display_menu(fin):
    if fin.current is None:
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')
    else:
        print('1. Balance')
        print('2. Log out')
        print('0. Exit')


def display_balance(fin):
    balance = bank.Bank.balance(fin)
    print(f'\nBalance: {balance}\n')


def create_client(fin):
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
