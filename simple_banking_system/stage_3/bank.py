from client import Client
import sqlite3


class Bank:
    def __init__(self):
        self.client = None
        self.client_logged = False

    def update_db(self, client):
        """Updates the database (list) of clients"""
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute("""INSERT INTO card 
                            (number, pin) 
                        VALUES (
                            :number, 
                            :pin
                        )""",
                    {
                        'number': client.card_number,
                        'pin': client.pin
                    }
                    )
        conn.commit()
        conn.close()

    def balance(self):
        """Returns the balance"""
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute("""SELECT
                        balance
                    FROM
                        card
                    WHERE
                        :number=number""",
                    {'number': self.client}
                    )
        balance = cur.fetchone()
        return balance[0]

    def log_in(self):
        """Returns whether the client has been logged in"""
        card_number = input('Enter your card number:\n')
        pin = input('Enter your PIN:\n')
        # checks if number exists in db and pin corresponds to it
        conn = sqlite3.connect('card.s3db')
        cur = conn.cursor()
        cur.execute("""SELECT 
                        number, 
                        pin 
                    FROM 
                        card 
                    WHERE 
                        :number=number
                        AND :pin=pin""",
                    {
                        'number': card_number,
                        'pin': pin
                    }
                    )
        result = cur.fetchone()
        conn.close()
        if result:
            self.client = result[0]
            self.client_logged = True
            return True
        else:
            return False

    def log_out(self):
        """Returns True if a client has been logged out"""
        self.client = None
        self.client_logged = False
        return True
