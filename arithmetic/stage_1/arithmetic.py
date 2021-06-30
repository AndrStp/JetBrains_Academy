class Calculator:
    def __init__(self):
        self.operators = ['+', '-', '*']

    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def take_input(self):
        """Return the operands (int) and operator"""
        a, operator, b = input().split()
        return int(a), int(b), operator

    def run(self, a, b, operator):
        """Perform the calculation"""
        if operator in self.operators:
            if operator == '+':
                return self.add(a, b)
            elif operator == '-':
                return self.substract(a, b)
            else:
                return self.multiply(a, b)


mini_calc = Calculator()
a, b, operator = mini_calc.take_input()
print(mini_calc.run(a, b, operator))