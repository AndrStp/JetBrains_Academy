from random import choice

def main():
    stock, computer, player, snake, status = initialize()
    status, high_piece = player_status(computer, player)
    snake.append(high_piece)

    if status == 'None':
        main()

    if status == 'player':
        player.remove(high_piece)
    else:
        computer.remove(high_piece)

    display(stock, computer, player, snake, status)


def initialize():
    """Initialize the starting pieces"""
    DOMINO_SET = [[x, y] for x in range(7) for y in range(x, 7)]

    stock = []
    computer = []
    player = []
    snake = []
    status = None

    for i in range(7):
        piece = choice(DOMINO_SET)
        computer.append(piece)
        DOMINO_SET.remove(piece)

        piece = choice(DOMINO_SET)
        player.append(piece)
        DOMINO_SET.remove(piece)

    stock = DOMINO_SET[:]

    return stock,computer,player,snake,status


def player_status(computer: list, player: list):
    """Define the one who makes the first move player"""
    comp_doubles = []
    for piece in computer:
        if piece[0] == piece[1]:
            comp_doubles.append(piece)
    
    player_doubles = []
    for piece in player:
        if piece[0] == piece[1]:
            player_doubles.append(piece)

    if not comp_doubles and not player_doubles:
        return None, None
    else:
        if not comp_doubles:
            return 'computer', max(player_doubles)
        elif not player_doubles:
            return 'player', max(comp_doubles)
        else:
            highest_piece = max(max(comp_doubles), max(player_doubles))
            if highest_piece in player_doubles:
                return 'computer', max(player_doubles)
            else:
                return 'player', max(comp_doubles)


def display(stock, computer, player, snake, status):
    """Displays the result so far"""
    print('Stock pieces:', stock)
    print('Computer pieces:', computer)
    print('Player pieces:', player)
    print('Domino snake:', snake)
    print('Status:', status)


if __name__ == '__main__':
    main()