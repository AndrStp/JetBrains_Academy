class CoffeeMachine():
    def __init__(self):
        self.water = None
        self.milk = None
        self.beans = None

    def read_inventory(self):
        self.water = int(input('Write how many ml of water the coffee machine has:\n'))
        self.milk = int(input('Write how many ml of milk the coffee machine has:\n'))
        self.beans = int(input('Write how many grams of coffee beans the coffee machine has:\n'))

    def calc_cups(self) -> int:
        cups_w = self.water // 200
        cups_m = self.milk // 50
        cups_b = self.beans // 15
        return min(cups_w, cups_m, cups_b)

    def make_coffee(self):
        cups_needed = int(input('Write how many cups of coffee you will need:\n'))
        cups = self.calc_cups()
        if cups > cups_needed:
            print(f'Yes, I can make that amount of coffee (and even {cups - cups_needed} more than that)')
            return
        elif cups == cups_needed:
            print('Yes, I can make that amount of coffee ')
            return
        else:
            print(f'No, I can make only {cups} cups of coffee')


coffee = CoffeeMachine()
coffee.read_inventory()
coffee.make_coffee()
