def main():
    final_string = []
    while len(final_string) < 100:
        print('Print a random string containing 0 or 1:\n')
        string = list(input())
        for char in string:
            if char.isdigit() and int(char) in {0, 1}:
                final_string.append(char)
        print(f'Current data length is {len(final_string)}, {100 - len(final_string)} symbols left')
    print('Final data string:', ''.join(final_string), sep='\n')


if __name__ == '__main__':
    main()
