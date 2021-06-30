import random


class Calculator:
    def __init__(self):
        self.operators = ['+', '-', '*']
        self.attempts = 5
        self.lvls = {
            1: 'simple operations with numbers 2-9',
            2: 'integral squares of 11-29'
        }
        self.chosen_lvl = None

    def run_calc(self):
        """Runs the calculator. Displays the result"""
        self.chose_level()
        mark = 0
        for i in range(self.attempts):
            expression = self.generate_expression()
            result = self.perform_calc(expression)
            print(expression)
            while True:
                try:
                    answer = int(input())
                    if answer == result:
                        mark += 1
                        print('Right!')
                        break
                    else:
                        print('Wrong!')
                        break
                except ValueError:
                    print('Incorrect format.')
        print(f'Your mark is {mark}/{self.attempts}.',
              'Would you like to save the result? Enter yes or no.')
        option = input().lower()
        if option in ['yes', 'y']:
            name = input('What is your name?\n')
            self.write_to_file(name, mark)
            print('The results are saved in "results.txt".')

    def chose_level(self):
        """Return the difficulty level and display the menu"""
        print('Which level do you want? Enter a number:')
        for key, value in self.lvls.items():
            print(key, value, sep=' - ')
        while True:
            try:
                lvl = int(input())
                if 2 >= lvl >= 1:
                    self.chosen_lvl = list(self.lvls.items())[lvl - 1]
                    return
                else:
                    print('Incorrect format.')
            except ValueError:
                print('Incorrect format.')

    def add(self, a, b) -> int:
        return a + b

    def substract(self, a, b) -> int:
        return a - b

    def multiply(self, a, b) -> int:
        return a * b

    def power(self, a) -> int:
        return a ** 2

    def perform_calc(self, expression: str) -> int:
        """Perform the calculation"""
        if self.chosen_lvl[0] == 1:
            a, operator, b = expression.split()
            a, b = int(a), int(b)
            if operator in self.operators:
                if operator == '+':
                    return self.add(a, b)
                elif operator == '-':
                    return self.substract(a, b)
                else:
                    return self.multiply(a, b)
        else:
            return self.power(int(expression))

    def generate_expression(self) -> str:
        """Return the expression to solve"""
        if self.chosen_lvl[0] == 1:
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            operator = random.choice(self.operators)
            return f'{a} {operator} {b}'
        else:
            return str(random.randint(11, 29))

    def write_to_file(self, name: str, mark: int):
        """Save the result to the file 'results.txt'"""
        with open('results.txt', 'a') as f:
            f.write(f'{name.capitalize()}: {mark}/{self.attempts} in level {self.chosen_lvl[0]} ({self.chosen_lvl[1]})')


mini_calc = Calculator()
mini_calc.run_calc()
