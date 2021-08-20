def main():
    """Runs the game"""
    width, height = take_dimensions()
    board = make_board(width, height)
    cell_size = len(board[0][0])

    while True:
        position = take_position(board)
        if not position:
            print()
            continue
        else:
            break

    board = set_starting_point(board, cell_size, position)
    pos_moves = find_possible_move(board, position)
    board = mark_possible_moves(board, cell_size, pos_moves)
    display_board(board, cell_size)


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
    cell = '_' * len(str(cell_number))
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


def into_chess(board: list, coordinates: tuple) -> tuple:
    """Return the coordinates for chess board"""
    column, row = coordinates[0] + 1, abs(len(board) - coordinates[1])
    return column, row


def into_index(board: list, coordinates: tuple) -> tuple:
    """Return the list indexes for internal representation"""
    inner, outer = coordinates[0] - 1, abs(coordinates[1] - len(board))
    return inner, outer


def set_starting_point(board: list, cell_size: int, coordinates: tuple) -> list:
    """Return the chess board with the inserted knight's position"""
    inner, outer = into_index(board, coordinates)
    board[outer][inner] = (cell_size - 1) * ' ' + 'X'
    return board


def mark_possible_moves(board: list, cell_size: int, moves: list) -> list:
    """Return the chess board with the possible moves marked with letter O"""
    for move in moves:
        inner, outer = into_index(board, move)
        board[outer][inner] = (cell_size - 1) * ' ' + 'O'
    return board


def find_possible_move(board: list, starting_point: tuple) -> list:
    """Returns the list of valid moves for knight from starting_point"""
    row, column = starting_point
    knight_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    moves = []
    for move in knight_moves:
        pos_row = row + move[0]
        if pos_row > len(board[0]) or pos_row < 1:
            continue
        pos_column = column + move[1]
        if pos_column > len(board) or pos_column < 1:
            continue
        moves.append((pos_row, pos_column))

    return moves


def display_board(board: list, cell_size: int) -> None:
    """Displays the chess board (i.e. start counting from 1 to 8 and
    from left to right and from bottom to top"""
    border = ' ' + '-' * (len(board[0]) * (cell_size + 1) + 3)

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
