from copy import copy
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

    def create_number(self) -> str:
        seed()
        IIN = 400000
        card_number = [int(x) for x in str(IIN)]
        for i in range(9):
            card_number.append(randint(1, 9))
        checksum = self.luhn_algo(copy(card_number))
        card_number.append(checksum)
        card_number = [str(i) for i in card_number]
        return ''.join(card_number)

    def luhn_algo(self, number: list) -> int:
        for i in range(len(number)-1, -1, -2):
            number[i] *= 2
            if number[i] > 9:
                number[i] -= 9
        sum_number = sum(number)
        temp = sum_number % 10
        if temp == 0:
            checksum = 0
        else:
            checksum = 10 - temp
        return checksum

    def is_valid_num(self, number: str) -> bool:
        number = [int(x) for x in copy(number)]
        check_sum = number.pop()
        for i in range(len(number)-1, -1, -2):
            number[i] *= 2
            if number[i] > 9:
                number[i] -= 9
        sum_number = sum(number) + check_sum
        if sum_number % 10 == 0:
            return True
        else:
            return False

    def create_pin(self) -> str:
        seed()
        pin = []
        for i in range(4):
            pin.append(randint(1, 9))
        pin = [str(i) for i in pin]
        return ''.join(pin)
