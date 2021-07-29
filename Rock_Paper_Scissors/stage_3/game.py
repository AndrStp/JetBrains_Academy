from random import choice


class Game:
    def __init__(self):
        self.options = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}
        self.player_move = None
        self.computer_move = None

    def take_player_move(self):
        """Takes a move from a user"""
        while True:
            move = input()
            if move not in self.options.keys() and move != '!exit':
                print('Invalid input')
            else:
                self.player_move = move
                return

    def winner(self):
        """Picks a winner"""
        self.computer_move = choice([option for option in self.options.keys()])
        if self.player_move == self.computer_move:
            return f'There is a draw ({self.player_move})'
        elif self.options[self.player_move] == self.computer_move:
            return f'Sorry, but the computer chose {self.computer_move}'
        else:
            return f'Well done. The computer chose {self.computer_move} and failed'


    def play_game(self):
        """Runs the game"""
        while True:
            self.take_player_move()
            if self.player_move == '!exit':
                print('Bye!')
                return
            game_outcome = self.winner()
            print(game_outcome)


rps_game = Game()
rps_game.play_game()
