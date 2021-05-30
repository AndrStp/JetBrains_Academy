from random import choice, randint


def main():
    domino_set = [[x, y] for x in range(7) for y in range(x, 7)]
    stock, computer, player = initialize(domino_set)

    snake = []
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

    while True:
        display_result(stock, computer, player, snake)
        rslt = is_winner(computer, player)
        if rslt == 'computer':
            print("Status: The game is over. The computer won!")
            break
        elif rslt == 'player':
            print("Status: The game is over. You won!")
            break
        rslt = is_draw(snake)
        if rslt == 'draw':
            print("Status: The game is over. It's a draw!")
            break

        if status == 'player':
            print("Status: It's your turn to make a move. Enter your command.")
            domino_num, negative = take_move(player)
            if domino_num != 0:
                snake, player = move_player(domino_num, negative, snake, player)
            else:
                stock, player = take_extra(stock, player)
            status = 'computer'
        else:
            print("Status: Computer is about to make a move. Press Enter to continue...")
            snake, status = move_comp(snake, computer)
            status = 'player'


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


def move_player(domino_num: int, negative: bool, snake_p: list, player_p: list):
    """Handles a player's move logic"""
    # if domino_num in range(1, len(player_p) + 1):
    if negative:
        snake_p.insert(0, player_p[domino_num - 1])
        player_p.pop(domino_num - 1)
    else:
        snake_p.append(player_p[domino_num - 1])
        player_p.pop(domino_num - 1)
    return snake_p, player_p


def take_move(player_p):
    """Handles input"""
    while True:
        try:
            raw = int(input())
        except ValueError:
            print('Invalid input. Please try again.')
            continue
        if raw not in range(-len(player_p), len(player_p) + 1):
            print('Enter a valid number')
            continue
        negative = raw < 0
        domino_num = abs(raw) if negative else raw
        return domino_num, negative


def move_comp(snake_p: list, computer_p: list):
    """Handles the computer move's logic"""
    temp = input()
    move = randint(-len(computer_p), len(computer_p))
    negative = move < 0
    domino_num = abs(move) if negative else move
    if negative:
        snake_p.insert(0, computer_p[domino_num - 1])
        computer_p.pop(domino_num - 1)
    else:
        snake_p.append(computer_p[domino_num - 1])
        computer_p.pop(domino_num - 1)
    return snake_p, computer_p


def take_extra(stock_p: list, player_p: list):
    """Adds a piece from a stock to a gamer's list"""
    piece = choice(stock_p)
    player_p.append(piece)
    stock_p.remove(piece)
    return stock_p, player_p


def is_winner(computer_p: list, player_p: list):
    """Returns the player who won"""
    if len(computer_p) == 0:
        return 'computer'
    elif len(player_p) == 0:
        return 'player'


def is_draw(snake_p: list):
    """Checks whether it is a draw"""
    edge = snake_p[0][0]
    if edge == snake_p[-1][-1]:
        counter = sum(p.count(edge) for p in snake_p)
        if counter == 8:
            return 'draw'


def display_player(player_p: list):
    """Displays the player's pieces to the prompt"""
    temp = (piece for piece in enumerate(player_p, start=1))
    print('Your pieces:')
    for i in temp:
        print(i[0], i[1], sep=':',)


def display_snake(snake: list):
    """Displays the current snake.
    If len of snake > 6 returns only first and last 3 pieces"""
    if len(snake) > 6:
        print(*snake[:3], '...', *snake[-3:], sep='')
    else:
        print(*snake, sep='')
    print()


def display_result(stock_a, computer_p, player_p, snake_p):
    """The game's interface"""
    print('=' * 70)
    print('Stock size: ', len(stock_a))
    print('Computer pieces: ', len(computer_p), '\n')
    display_snake(snake_p)
    display_player(player_p)
    print()


if __name__ == '__main__':
    main()
    # domino_set = [[x, y] for x in range(7) for y in range(x, 7)]
    # stock, computer, player = initialize(domino_set)
    # snake = []
    # highest = (snake_piece(computer, player))
    # if highest == 'reshuffle':
    #     main()
    # else:
    #     snake.append(highest)

    # status = first_move(snake, computer)
    # if status == "computer":
    #     player.remove(highest)
    # else:
    #     computer.remove(highest)