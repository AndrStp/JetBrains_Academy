class TicTacToe:
    def __init__(self):
        self.table = [' ' for _ in range(9)]  # using 1-d list
        self.player = 'X'  # the one who makes the first move, normally 'X'

    def fill_table(self):
        """Returns table with cells"""
        move = input('Enter cells: ')
        for count, cell in enumerate(move):
            self.table[count] = cell

    def make_move(self):
        """Insert the 'X' / 'O' to the given coordinate (row column) to the table"""
        while True:
            try:
                row, column = (int(value) for value in input('Enter the coordinates: ').split())
                if row > 3 or column > 3:
                    print('Coordinates should be from 1 to 3!')
                    continue
                index = self.convert_input(row, column)
                if self.table[index] != ' ':
                    print('This cell is occupied! Choose another one!')
                else:
                    if self.player == 'X':
                        self.table[index] = 'X'
                        self.player = 'O'
                    else:
                        self.table[index] = 'O'
                        self.player = 'X'
                    return
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

        for position in win_positions:
            if all([cell == 'X' for cell in position]):
                return 'X'

        for position in win_positions:
            if all([cell == 'O' for cell in position]):
                return 'O'

    def available_moves(self) -> int:
        """Returns the number of free spaces left in the table"""
        return self.table.count(' ')

    def display_table(self):
        """Displays board to the terminal"""
        print('-' * 9)
        for row in [self.table[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' '.join(row) + ' |')
        print('-' * 9)

    def play(self):
        """Handles the game (main)"""
        self.display_table()
        self.make_move()
        self.display_table()
        game_finished = False
        while not game_finished:
            self.make_move()
            self.display_table()
            win = self.game_over()
            if win:
                print(win, 'wins')
                game_finished = True
            elif self.available_moves() == 0:
                print('Draw')
                game_finished = True


game = TicTacToe()
game.play()
