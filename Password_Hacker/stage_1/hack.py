import argparse
import socket


def main():
    hostname, port, message = read_args()
    response = client(hostname, port, message)
    print(response)


def client(hostname, port, message) -> str:
    """
    Send and receive the message from the server
    :param hostname: ip_address of the server
    :param port: port number to connect
    :param message: message to send
    :return: response from the server
    """
    with socket.socket() as s:
        s.connect((hostname, port))
        message = message.encode()
        s.send(message)
        response = s.recv(1024).decode()

    return response


def read_args():
    """
    :return: tuple of ip_address, port and message
    """
    parser = argparse.ArgumentParser(description='Password Hacker')
    parser.add_argument('ip_address', type=str, help='IP address')
    parser.add_argument('port', type=int, help='port number')
    parser.add_argument('message', type=str, help='message to send')
    args = parser.parse_args()

    return args.ip_address, args.port, args.message


if __name__ == '__main__':
    main()
