class CoffeeMachine():
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def take_action(self) -> str:
        """Reads the action from the user"""
        action = input('Write action (buy, fill, take):\n')
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

    def make_coffee(self):
        option = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n'))
        self.cups -= 1
        if option == 1:
            # 250 water, 16 beans, $4
            self.water -= 250
            self.beans -= 16
            self.money += 4
        elif option == 2:
            # 350 water, 75 milk, 20 beans, $7
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
        elif option == 3:
            # 200 water, 100 milk, 12 beans, $6
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6

    def display_inventory(self):
        print('The coffee machine has:',
              f'{self.water} of water',
              f'{self.milk} of milk',
              f'{self.beans} of beans',
              f'{self.cups} of disposable cups',
              f'{self.money} of money', sep='\n')
        print()

    def menu(self):
        self.display_inventory()
        option = self.take_action()
        if option == 'buy':
            self.make_coffee()
            print()
        elif option == 'fill':
            self.fill_inventory()
            print()
        else:
            money = self.take_money()
            print(f'I gave you ${money}\n')
        self.display_inventory()


coffee = CoffeeMachine()
coffee.menu()
