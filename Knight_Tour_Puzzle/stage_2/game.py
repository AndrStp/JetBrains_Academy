def main():
    """Runs the game"""
    width, height = take_dimensions()
    board = make_board(width, height)

    while True:
        position = take_position(board)
        if not position:
            print()
            continue
        else:
            break

    board = set_starting_point(board, position)
    display_board(board)


def take_dimensions() -> tuple:
    """Return the dimensions to construct the board"""
    while True:
        message = 'Invalid dimensions!'
        dimensions = input('Enter your board dimensions: ').split()
        if len(dimensions) != 2:
            print(message)
            continue

        check = all([dimension.isdigit() for dimension in dimensions])
        if check:
            width, height = int(dimensions[0]), int(dimensions[1])
            return width, height
        else:
            print(message)


def make_board(width: int, height: int) -> list:
    """Return the board with the given dimensions"""
    cell_number = width * height

    cell = None
    if len(str(cell_number)) == 1:
        cell = '_'
    elif len(str(cell_number)) == 2:
        cell = '__'
    else:
        cell = '___'

    board = [[cell for _ in range(width)] for _ in range(height)]
    return board


def take_position(board: list) -> tuple or bool:
    """Return the coordinates of the move"""
    while True:
        points = input('Enter the knight\'s starting position: ').split(' ')
        message = 'Invalid position!'
        if len(points) != 2:
            print(message)
            continue

        check = all([point.isdigit() for point in points])
        if not check:
            print(message)
            continue

        row, column = int(points[0]), int(points[1])
        if row not in range(1, len(board[0])+1) or column not in range(1, len(board)+1):
            print(message)
            continue

        return row, column


def set_starting_point(board: list, coordintates: tuple) -> list:
    """Return the chess board with the inserted knight's position"""
    column_point, row_point = coordintates[0], coordintates[1]
    column = column_point - 1
    row = abs(row_point - len(board))
    board[row][column] = board[row][column][:-1] + 'X'
    return board


def display_board(board: list) -> None:
    """Displays the chess board (i.e. start counting from 1 to 8 and
    from left to right and from bottom to top"""
    cell_size = len(board[0][0])
    border = '-' * (len(board[0]) * (cell_size + 1) + 3)

    print(border)
    for i, row in zip(reversed(range(1, len(board)+1)), board):
        if cell_size > 2:
            print(' ' * (2 - len(str(i))) + str(i) + '|', end=' ')
        else:
            print(str(i) + '|', end=' ')
        print(*row, sep=' ', end=' |\n')
    print(border)

    padding = ' ' * cell_size
    print('   ', end='')
    for i in range(1, len(board[0])+1):
        print(padding[:-(len(str(i)))] + str(i), end=' ')
    print()


if __name__ == '__main__':
    main()
