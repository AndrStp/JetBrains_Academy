from random import seed, randint


class Client:
    def __init__(self):
        self.card_number = self.create_number()
        self.pin = self.create_pin()
        self.card = {self.card_number: self.pin}
        self.balance = 0
        self.logged = False

    def __str__(self):
        return 'No.: ' + self.card_number + ' PIN: ' + self.pin

    def create_number(self):
        seed()
        IIN = 400000
        CHECKSUM = randint(1, 9)
        card_number = []
        for i in range(9):
            card_number.append(randint(1, 9))
        card_number.insert(0, IIN)
        card_number.append(CHECKSUM)
        card_number = [str(i) for i in card_number]
        return ''.join(card_number) # int() ?

    def create_pin(self):
        seed()
        pin = []
        for i in range(4):
            pin.append(randint(1, 9))
        pin = [str(i) for i in pin]
        return ''.join(pin) # int() ?
