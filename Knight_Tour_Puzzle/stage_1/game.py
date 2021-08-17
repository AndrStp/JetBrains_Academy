def main():
    """Runs the game"""
    board = [['_' for _ in range(8)] for _ in range(8)]

    position = take_position()
    if not position:
        print('Invalid dimensions!')
        quit()
    board = set_starting_point(board, position)
    display_board(board)


def take_position() -> tuple or bool:
    """Return the coordinates of the move"""
    user_input = input('Enter the knight\'s starting position: ').split(' ')
    if len(user_input) != 2:
        return False

    for point in user_input:
        if not point.isdigit():
            return False
        elif int(point) > 8:
            return False

    point_1, point_2 = int(user_input[0]), int(user_input[1])
    return point_1, point_2


def set_starting_point(board: list, coordintates: tuple) -> list:
    """Return the chess board with the inserted knight's position"""
    column_point, row_point = coordintates[0], coordintates[1]
    column = column_point - 1
    row = abs(row_point - 8)
    board[row][column] = 'X'
    return board


def display_board(board: list) -> None:
    """Displays the chess board (i.e. start counting from 1 to 8 and
    from left to right and from bottom to top"""
    border = ' ' + '-' * 19
    print(border)
    for i, row in zip(reversed(range(1, 9)), board):
        print(str(i) + '|', end=' ')
        print(*row, sep=' ', end=' |\n')
    print(border)
    print('   ', end='')
    print(*range(1, 9), sep=' ')


if __name__ == '__main__':
    main()
