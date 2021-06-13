class TicTacToe:
    def __init__(self):
        self.table = [' ' for _ in range(9)]
        self.player = 'player'
        self.computer = 'computer'

    def make_move(self):
        move = input('Enter cells: ')
        for count, cell in enumerate(move):
            self.table[count] = cell

    def display_table(self):
        print('-' * 9)
        for row in [self.table[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' '.join(row) + ' |')
        print('-' * 9)

    def play(self):
        self.make_move()
        self.display_table()


game = TicTacToe()
game.play()
