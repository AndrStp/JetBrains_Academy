from random import choice


class Game:
    def __init__(self):
        self.options = ['rock', 'paper', 'scissors']
        self.commands = ['!exit', '!rating']
        self.players = {}
        self.current_player_name = None
        self.current_player_score = None
        self.player_move = None
        self.computer_move = None

    def pick_player_options(self):
        """Initializes the player, score and playable options"""
        with open('rating.txt', 'r') as f_players:
            players = f_players.readlines()
            for player in players:
                player_name, player_score = player.strip().split()
                self.players[player_name] = int(player_score)
        # player and score
        user = input('Enter your name: ')
        self.current_player_name = user
        if user in self.players.keys():
            self.current_player_score = self.players[user]
        else:
            self.current_player_score = 0
        print('Hello,', user)
        # options
        options = input()
        if options != '':
            self.options = options.split(',')
        print("Okay, let's start")

    def take_input(self):
        """Takes and checks the input from the user"""
        while True:
            user_input = input()
            if user_input not in self.options and user_input not in self.commands:
                print('Invalid input')
            else:
                return user_input

    def process_user_input(self, user_input):
        """Process the input from the user"""
        if user_input in self.commands:
            if user_input == '!rating':
                print('Your rating:', self.current_player_score)
            elif user_input == '!exit':
                quit()
        else:
            self.player_move = user_input

    def winner(self):
        """Picks a winner"""
        self.computer_move = choice([option for option in self.options])
        comp_index = self.options.index(self.computer_move)
        middle_option = len(self.options) // 2
        player_option_index = self.options.index(self.player_move)
        position = player_option_index - middle_option
        altered_options = self.options[position:] + self.options[:position]
        win_options = altered_options[middle_option + 1:]
        lose_options = altered_options[:middle_option]

        if self.computer_move in lose_options:
            self.current_player_score += 100
            return f'Well done. The computer chose {self.computer_move} and failed'
        elif self.computer_move in win_options:
            return f'Sorry, but the computer chose {self.computer_move}'
        elif self.computer_move == self.player_move:
            self.current_player_score += 50
            return f'There is a draw ({self.player_move})'

    def play_game(self):
        """Runs the game"""
        self.pick_player_options()
        while True:
            user_input = self.take_input()
            self.process_user_input(user_input)
            game_outcome = self.winner()
            print(game_outcome)


rps_game = Game()
rps_game.play_game()
