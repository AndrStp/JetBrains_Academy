import random


def main():
    DEBUG = True
    final_string = take_input()
    print('\nFinal data string:', ''.join(final_string), sep='\n')
    print()
    print('\nPlease enter a test string containing 0 or 1:\n')
    test_str = input()
    prediction = predict(count_patterns(final_string), test_str)
    guessed, percentage = compare(prediction, test_str)
    print('\nprediction:')
    print(prediction)
    print()
    print(f'Computer guessed right {guessed} out of {len(test_str)} symbols ({percentage} %)')


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
    """Return triads stats"""
    patterns = {
        '000': [0, 0, 0],
        '001': [0, 0, 0],
        '010': [0, 0, 0],
        '011': [0, 0, 0],
        '100': [0, 0, 0],
        '101': [0, 0, 0],
        '110': [0, 0, 0],
        '111': [0, 0, 0]
    }
    sliced = [a_string[i:i+4] for i in range(0, len(a_string)) if len(a_string[i:i+4]) == 4]
    for el in sliced:
        if el[3:4] == '0':
            patterns[el[:3]][0] += 1
        else:
            patterns[el[:3]][1] += 1
    for v in patterns.values():
        v[2] = round((v[0] * 100 / (v[0] + v[1])), 2)
    return patterns


def predict(data: dict, test_str: str):
    """Return the predicted string based on the data"""
    prediction = ''.join((str(random.randint(0, 1)) for _ in range(3)))
    for i in range(3, len(test_str)):
        pattern = test_str[i - 3:i]
        probability = data[pattern][2]
        if probability > 50:
            prediction += "0"
        elif probability == 0.5:
            prediction += random.choice("01")
        else:
            prediction += "1"
    return prediction


def compare(prediction: str, test_str: str) -> float:
    """Return the accuracy of the predicted string"""
    guessed = 0
    for v1, v2, num in zip(test_str, prediction, range(len(test_str))):
        if (num >= 3) and (v1 == v2):
            guessed += 1
    accuracy = round(100 * guessed / (len(test_str) - 3), 2)
    return guessed, accuracy


if __name__ == '__main__':
    main()
