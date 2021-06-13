class TicTacToe:
    def __init__(self):
        self.table = [' ' for _ in range(9)]  # using 1-d list
        self.player = 'player'
        self.computer = 'computer'

    def fill_table(self):
        """Returns table with cells"""
        move = input('Enter cells: ')
        for count, cell in enumerate(move):
            self.table[count] = cell

    def make_move(self):
        """Insert the X to the given coordinate (row column) to the table"""
        while True:
            try:
                row, column = (int(value) for value in input('Enter the coordinates: ').split())
                if row > 3 or column > 3:
                    print('Coordinates should be from 1 to 3!')
                    continue
                index = self.convert_input(row, column)
                if self.table[index] != '_':
                    print('This cell is occupied! Choose another one!')
                else:
                    self.table[index] = 'X'
                    return True
            except ValueError:
                print('You should enter numbers!')

    def convert_input(self, row, column) -> int:
        """Return the index of the table by the given coordinate"""
        if row == 1:
            return column - 1
        if row == 2:
            return column + 2
        if row == 3:
            return column + 5

    def game_over(self):
        """Returns whether there is a winner"""
        win_positions = (
            [self.table[i*3: (i+1)*3] for i in range(3)] +
            [self.table[i: len(self.table): 3] for i in range(3)] +
            [[self.table[i] for i in [0, 4, 8]]] +
            [[self.table[i] for i in [2, 4, 6]]]
        )
        x_win = False
        for position in win_positions:
            if all([cell == 'X' for cell in position]):
                x_win = True

        o_win = False
        for position in win_positions:
            if all([cell == 'O' for cell in position]):
                o_win = True

        if x_win and o_win:
            print('Impossible')
            return True
        if x_win:
            print('X wins')
            return True
        if o_win:
            print('O wins')
            return True

    def impossible_position(self):
        x_num = self.table.count('X')
        o_num = self.table.count('O')
        if (x_num - o_num) > 1 or (o_num - x_num) > 1:
            print('Impossible')
            return True

    def available_moves(self):
        return self.table.count('_')

    def display_table(self):
        """Displays board to the terminal"""
        print('-' * 9)
        for row in [self.table[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' '.join(row) + ' |')
        print('-' * 9)

    def play(self):
        """Handles the game (main)"""
        self.fill_table()
        self.display_table()
        self.make_move()
        self.display_table()


game = TicTacToe()
game.play()
