import random


def main():
    print('Please give AI some data to learn...')
    learn_string = ''
    while len(learn_string) < 100:
        print(f'The current data length is {len(learn_string)}, {100 - len(learn_string)} symbols left')
        learn_string += take_input()
    game(learn_string)
    print('Game over!')


def game(learn_string: str):
    """Runs the game"""
    MONEY = 1000
    print('You have $1000. Every time the system successfully predicts your next press, you lose $1.')
    print('Otherwise, you earn $1. Print "enough" to leave the game.', 'Let\'s go!\n', sep='\n')
    while True:
        answer = take_input()
        if answer == 'enough':
            return
        data = count_patterns(learn_string)
        prediction = predict(data, answer)
        guessed, accuracy = compare(prediction, answer)
        MONEY = MONEY - 2 * guessed + len(prediction) - 3
        print('prediction:')
        print(prediction)
        print()
        print(f'Computer guessed right {guessed} out of {len(answer) - 3} symbols ({accuracy} %)\n')
        print(f'Your capital is now ${MONEY}')
        data = correct_data(data, answer)


def take_input() -> str:
    """Return the preprocessed string from the user """
    print('Print a random string containing 0 or 1:\n')
    string = list(input())
    if ''.join(string) == 'enough':
        return 'enough'
    final_string = []
    for char in string:
        if char.isdigit() and int(char) in {0, 1}:
            final_string.append(char)
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
    for val in patterns.values():
        if val[0] != 0 or val[1] != 0:
            val[2] = round((val[0] * 100 / (val[0] + val[1])), 2)
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


def compare(prediction: str, test_str: str):
    """Return the number of correct predictions and accuracy of the predicted string"""
    guessed = 0
    for v1, v2, num in zip(test_str, prediction, range(len(test_str))):
        if (num >= 3) and (v1 == v2):
            guessed += 1
    accuracy = round(100 * guessed / (len(test_str) - 3), 2)
    return guessed, accuracy


def correct_data(data: dict, answer: str) -> dict:
    temp = count_patterns(answer[:-3])
    for key, val in temp.items():
        data[key][0] += temp[key][0]
        data[key][1] += temp[key][1]
        if val[0] != 0 or val[1] != 0:
            val[2] = round((val[0] * 100 / (val[0] + val[1])), 2)
    return data


if __name__ == '__main__':
    main()
