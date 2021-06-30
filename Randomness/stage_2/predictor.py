def main():
    final_string = take_input()
    print('\nFinal data string:', ''.join(final_string), sep='\n')
    triads = count_patterns(final_string)
    print()
    for key, value in triads.items():
        print(f'{key}: {value[0]},{value[1]}')


def take_input() -> str:
    final_string = []
    while len(final_string) < 100:
        print('Print a random string containing 0 or 1:\n')
        string = list(input())
        for char in string:
            if char.isdigit() and int(char) in {0, 1}:
                final_string.append(char)
        if len(final_string) < 100:
            print(f'Current data length is {len(final_string)}, {100 - len(final_string)} symbols left')
    return ''.join(final_string)


def count_patterns(a_string: str) -> dict:
    triads = {
        '000': [0, 0],
        '001': [0, 0],
        '010': [0, 0],
        '011': [0, 0],
        '100': [0, 0],
        '101': [0, 0],
        '110': [0, 0],
        '111': [0, 0]
    }
    sliced = [a_string[i:i+4] for i in range(0, len(a_string)) if len(a_string[i:i+4]) == 4]
    for el in sliced:
        if el[3:4] == '0':
            triads[el[:3]][0] += 1
        else:
            triads[el[:3]][1] += 1
    return triads


if __name__ == '__main__':
    main()
