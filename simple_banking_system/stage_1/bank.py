from client import Client


class Bank:
    def __init__(self):
        self.clients = []
        self.current = None

    def update_db(self, client):
        self.clients.append(client)

    def balance(self):
        return self.current.balance

    def log_in(self):
        card_number = input('Enter your card number:\n')
        for client in self.clients:
            if card_number in client.card:
                pin = input('Enter your PIN:\n')
                if pin == client.card[card_number]:
                    self.current = client
                    self.current.logged = True
                    return True
                else:
                    return False
        else:
            return False

    def log_out(self):
        self.current.logged = False
        self.current = None
        return True
