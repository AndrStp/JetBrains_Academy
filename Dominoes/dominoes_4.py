from hashlib import algorithms_available
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
        outcome = {
            'computer': "Status: The game is over. The computer won!",
            'player': "Status: The game is over. You won!"
        }
        if rslt in outcome:
            print(outcome[rslt])
            break
        rslt = is_draw(snake)
        if rslt == 'draw':
            print("Status: The game is over. It's a draw!")
            break

        if status == 'player':
            print("Status: It's your turn to make a move. Enter your command.")
            while True:
                negative, piece = take_move_player(player)
                if piece == 'extra':
                    stock, player = take_extra(stock, player)
                    break
                else:
                    legal = legal_move(snake, piece, negative)
                    if legal:
                        player.remove(piece)
                        snake = change_snake(snake, piece, negative)
                        break
                    else:
                        print('Illegal move. Please try again.')
                        continue
            status = 'computer'
        else:
            print("Status: Computer is about to make a move. Press Enter to continue...")
            temp = input()
            while True:
                negative, piece = move_comp(snake, computer)
                if piece == 'extra':
                    if not stock:
                        break
                    else:
                        stock, computer = take_extra(stock, computer)
                        break
                else:
                    legal = legal_move(snake, piece, negative)
                    if legal:
                        computer.remove(piece)
                        snake = change_snake(snake, piece, negative)
                        break
                    else:
                        continue
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


def first_move(snake: list, computer_p: list) -> str:
    """Return the player that should take the next move"""
    if snake[0] in computer_p:
        return 'player'
    else:
        return 'computer'


def take_move_player(player_p: list):
    """Handles input"""
    while True:
        try:
            raw = int(input())
        except ValueError:
            print('Invalid input. Please try again.')
            continue
        if raw not in range(-len(player_p), len(player_p) + 1):
            print('Invalid input. Please try again.')
            continue
        negative = raw < 0
        domino_num = abs(raw) if negative else raw
        if domino_num == 0:
            return negative, 'extra'
        else:
            return negative, player_p[domino_num - 1]


def move_comp(snake_p: list, computer_p: list):
    """Handles the computer move's logic"""
    while True:
        snake_head = snake_p[0][0]
        snake_tail = snake_p[-1][-1]
        available_moves = 0
        for piece in computer_p:
            for num in piece:
                if num == snake_head or num == snake_tail:
                    available_moves += 1
        if not available_moves:
            return 'None', 'extra'
        move = randint(-len(computer_p), len(computer_p))
        if move == 0:
            continue
        negative = move < 0
        domino_num = abs(move) if negative else move
        return negative, computer_p[domino_num - 1]


def change_snake(snake_p: list, domino_piece: list, negative: bool) -> list:
    """Adds a given domino to a snake"""
    if negative:
        if domino_piece[-1] == snake_p[0][0]:
            snake_p.insert(0, domino_piece)
        else:
            domino_piece[0], domino_piece[-1] = domino_piece[-1], domino_piece[0]
            snake_p.insert(0, domino_piece)
    else:
        if domino_piece[0] == snake_p[-1][-1]:
            snake_p.append(domino_piece)
        else:
            domino_piece[0], domino_piece[-1] = domino_piece[-1], domino_piece[0]
            snake_p.append(domino_piece)
    return snake_p


def legal_move(snake_p: list, domino_piece: list, negative: bool) -> bool:
    """Checks whether the move is legal"""
    if negative:
        for num in domino_piece:
            if num == snake_p[0][0]:
                return True
        else:
            return False
    else:
        for num in domino_piece:
            if num == snake_p[-1][-1]:
                return True
        else:
            return False  


def take_extra(stock_p: list, gamer: list):
    """Adds a piece from a stock to a gamer's list"""
    piece = choice(stock_p)
    gamer.append(piece)
    stock_p.remove(piece)
    return stock_p, gamer


def is_winner(computer_p: list, player_p: list) -> str:
    """Returns the player who won"""
    if len(computer_p) == 0:
        return 'computer'
    elif len(player_p) == 0:
        return 'player'


def is_draw(snake_p: list) -> str:
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
