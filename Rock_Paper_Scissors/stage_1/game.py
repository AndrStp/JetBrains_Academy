class Game:
    def __init__(self):
        self.options = {'rock': 'paper', 'scissors': 'rock', 'paper': 'scissors'}

    @staticmethod
    def take_input():
        """Takes a move from a user"""
        move = input()
        return move

    @staticmethod
    def display(game_outcome):
        """Displays the result of the game"""
        print(f'Sorry, but the computer chose {game_outcome}')

    def outcome(self, move):
        """Returns whether the player has won the game"""
        if move in self.options:
            return self.options[move]

    def play_game(self):
        """Runs the game"""
        move = self.take_input()
        game_outcome = self.outcome(move)
        self.display(game_outcome)


rps_game = Game()
rps_game.play_game()
