class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def take_action(self) -> str:
        """Reads the action from the user"""
        action = input('Write action (buy, fill, take, remaining, exit):\n')
        return action

    def fill_inventory(self):
        """Updates the inventory"""
        self.water += int(input('Write how many ml of water you want to add:\n'))
        self.milk += int(input('Write how many ml of you want to add:\n'))
        self.beans += int(input('Write how many grams of coffee beans you want to add:\n'))
        self.cups += int(input('Write how many disposable coffee cups you want to add:\n'))

    def take_money(self):
        """Take all the money from the register"""
        money = self.money
        self.money = 0
        return money

    def take_menu(self):
        option = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n').lower()
        if option == 'back':
            return None
        return option

    def make_coffee(self, option):
        """Makes coffee"""
        menu = {'1': 'espresso', '2': 'latte', '3': 'cappuccino'}
        insuff = self.check_supplies(menu.get(option))
        if insuff:
            return insuff
        else:
            self.cups -= 1
            if option == '1':
                # 250 water, 16 beans, $4
                self.water -= 250
                self.beans -= 16
                self.money += 4
            elif option == '2':
                # 350 water, 75 milk, 20 beans, $7
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
            elif option == '3':
                # 200 water, 100 milk, 12 beans, $6
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6

    def check_supplies(self, option):
        """Returns whether it is possible to serve make a particular drink"""
        recipe = {
            'espresso': {'water': 250, 'beans': 16},
            'latte': {'water': 350, 'milk': 75, 'beans': 20},
            'cappuccino': {'water': 200, 'milk': 100, 'beans': 12}
        }
        supplies = {'water': self.water, 'milk': self.milk, 'beans': self.beans}
        # if we don't have enough cups return False
        if self.cups == 0:
            return 'cups'
        else:
            for position, value in recipe[option].items():
                if supplies[position] < value:
                    return position

    def display_inventory(self):
        print('The coffee machine has:',
              f'{self.water} of water',
              f'{self.milk} of milk',
              f'{self.beans} of beans',
              f'{self.cups} of disposable cups',
              f'{self.money} of money', sep='\n')
        print()

    def run_machine(self):
        """Main method"""
        while True:
            option = self.take_action()
            print()
            if option == 'buy':
                rslt = self.take_menu()
                if rslt:
                    insuff = self.make_coffee(rslt)
                    if insuff is None:
                        print('I have enough resources, making you a coffee!')
                    else:
                        print(f'Sorry, not enough {insuff}!')
                else:
                    print()
                    continue
                print()
            elif option == 'fill':
                self.fill_inventory()
                print()
            elif option == 'take':
                money = self.take_money()
                print(f'I gave you ${money}\n')
            elif option == 'remaining':
                self.display_inventory()
            else:
                return


coffee = CoffeeMachine()
coffee.run_machine()
