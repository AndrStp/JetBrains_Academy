from random import choice


def main():
    domino_set = [[x, y] for x in range(7) for y in range(x, 7)]
    snake = []
    stock, computer, player = initialize(domino_set)

    highest = (snake_piece(computer, player))
    if highest == 'reshuffle':
        main()
    else:
        snake.append(highest)

    status = first_move(snake, computer)
    if status == "computer":
        player.remove(highest)
    else:
        computer.remove(highest)

    display_result(stock, computer, player, snake, status)


def initialize(starting_pieces: list):
    """Initializes the starting positions of the games"""
    computer = []
    player = []

    for i in range(7):
        piece = choice(starting_pieces)
        computer.append(piece)
        starting_pieces.remove(piece)

        piece = choice(starting_pieces)
        player.append(piece)
        starting_pieces.remove(piece)

    stock = starting_pieces[:]

    return stock, computer, player


def snake_piece(computer_p: list, player_p: list):
    """Return the snake (starting) piece"""
    comp_doubles = []
    player_doubles = []
    for piece_1, piece_2 in zip(computer_p, player_p):
        if piece_1[0] == piece_1[1]:
            comp_doubles.append(piece_1)
        if piece_2[0] == piece_2[1]:
            player_doubles.append(piece_2)

    if not (comp_doubles or player_doubles):
        return 'reshuffle'
    if comp_doubles and not player_doubles:
        return max(comp_doubles)
    if player_doubles and not comp_doubles:
        return max(player_doubles)
    else:
        return max(max(comp_doubles), max(player_doubles))


def first_move(snake: list, computer_p: list):
    """Return the player that should take the next move"""
    if snake[0] in computer_p:
        return 'player'
    else:
        return 'computer'


def display_player(player_p: list):
    """Displays the player's pieces to the prompt"""
    temp = (piece for piece in enumerate(player_p, start=1))
    print('Your pieces:')
    for i in temp:
        print(i[0], i[1], sep=':',)


def display_result(stock_a, computer_p, player_p, snake_p, status_a):
    if status_a == 'player':
        message = "Status: It's your turn to make a move. Enter your command."
    else:
        message = "Status: Computer is about to make a move. Press Enter to continue..."
    print('=' * 70)
    print('Stock size: ', len(stock_a))
    print('Computer pieces: ', len(computer_p), '\n')
    print(snake_p[0], '\n')
    display_player(player_p)
    print()
    print(message)


if __name__ == '__main__':
    main()
    # domino_set = [[x, y] for x in range(7) for y in range(x, 7)]
    # snake = []
    # stock, computer, player = initialize(domino_set)
