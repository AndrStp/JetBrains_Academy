import random


class Calculator:
    def __init__(self):
        self.operators = ['+', '-', '*']
        self.nums = [str(i) for i in range(2, 10)]

    def add(self, a, b) -> int:
        return a + b

    def substract(self, a, b) -> int:
        return a - b

    def multiply(self, a, b) -> int:
        return a * b

    def take_expr(self, expr: str):
        """Return the operands (int) and operator"""
        a, operator, b = expr.split()
        return int(a), int(b), operator

    def run_calc(self, a, b, operator) -> int:
        """Perform the calculation"""
        if operator in self.operators:
            if operator == '+':
                return self.add(a, b)
            elif operator == '-':
                return self.substract(a, b)
            else:
                return self.multiply(a, b)

    def generate_expression(self) -> str:
        """Return the expression to solve"""
        a = random.choice(self.nums)
        b = random.choice(self.nums)
        operator = random.choice(self.operators)
        return f'{a} {operator} {b}'

    def stage_task(self):
        expression = self.generate_expression()
        a, b, operator = self.take_expr(expression)
        result = self.run_calc(a, b, operator)
        print(expression)
        answer = int(input())
        if answer == result:
            print('Right!')
        else:
            print('Wrong!')


mini_calc = Calculator()
mini_calc.stage_task()


