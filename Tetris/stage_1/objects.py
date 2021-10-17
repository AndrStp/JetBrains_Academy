# import numpy as np  # np.arange(16).reshape(4, 4)


class Grid:
    def __init__(self) -> None:
        self.grid = [['-' for _ in range(4)] for _ in range(4)]
        self.letter = None

    def __str__(self):
        result = ''
        for row in self.grid:
            for el in row:
                result += el + ' '
            result = result.rstrip()
            result += '\n'
        return result

    def __repr__(self):
        return str(self.grid)

    def take_letter(self, other) -> None:
        self.letter = other

    def display_letter(self) -> None:
        for form in self.letter.forms:
            self.reset()
            for i, j in form:
                self.grid[i][j] = '0'
            print(self)

    def reset(self) -> None:
        """Resets the grid to default"""
        self.grid = [['-' for _ in range(4)] for _ in range(4)]


class Letter:
    def __init__(self, name: str) -> None:
        if name.upper() not in {'I', 'S', 'Z', 'L', 'J', 'O', 'T'}:
            raise ValueError('Incorrect letter')
        self.name = name.upper()
        self.forms = None

    def __repr__(self):
        return str(self.name)

    def set_form(self) -> None:
        global forms
        if self.name == 'I':
            forms = [
                [(0, 1), (1, 1), (2, 1), (3, 1)],
                [(1, 0), (1, 1), (1, 2), (1, 3)]
            ]

        if self.name == 'S':
            forms = [
                [(1, 2), (1, 1), (2, 1), (2, 0)],
                [(1, 1), (2, 1), (2, 2), (3, 2)]
            ]

        if self.name == 'Z':
            forms = [
                [(1, 0), (1, 1), (2, 1), (2, 2)],
                [(0, 2), (1, 2), (1, 1), (2, 1)],
                [(1, 0), (1, 1), (2, 1), (2, 2)],
                [(0, 2), (1, 2), (1, 1), (2, 1)],
                [(1, 0), (1, 1), (2, 1), (2, 2)],
            ]

        if self.name == 'O':
            forms = [
                [(1, 1), (1, 2), (2, 1), (2, 2)],
                [(1, 1), (1, 2), (2, 1), (2, 2)],
                [(1, 1), (1, 2), (2, 1), (2, 2)],
                [(1, 1), (1, 2), (2, 1), (2, 2)],
                [(1, 1), (1, 2), (2, 1), (2, 2)]
            ]

        if self.name == 'L':
            forms = [
                [(0, 1), (1, 1), (2, 1), (2, 2)],
                [(2, 0), (2, 1), (2, 2), (1, 2)],
                [(0, 1), (0, 2), (1, 2), (2, 2)],
                [(0, 0), (0, 1), (0, 2), (1, 0)],
                [(0, 1), (1, 1), (2, 1), (2, 2)]
            ]

        if self.name == 'J':
            forms = [
                [(0, 2), (1, 2), (2, 2), (2, 1)],
                [(1, 0), (1, 1), (1, 2), (2, 2)],
                [(0, 1), (0, 2), (1, 1), (2, 1)],
                [(0, 0), (1, 0), (1, 1), (1, 2)],
                [(0, 2), (1, 2), (2, 2), (2, 1)]
            ]

        if self.name == 'T':
            forms = [
                [(0, 1), (1, 0), (1, 1), (1, 2)],
                [(0, 1), (1, 0), (1, 1), (2, 1)],
                [(1, 0), (1, 1), (1, 2), (2, 1)],
                [(0, 1), (1, 1), (2, 1), (1, 2)],
                [(0, 1), (1, 0), (1, 1), (1, 2)]
            ]

        self.forms = forms


if __name__ == '__main__':
    grid = Grid()
    print(grid)
    letter = Letter('i')
    letter.set_form()
    grid.take_letter(letter)
    grid.display_letter()
