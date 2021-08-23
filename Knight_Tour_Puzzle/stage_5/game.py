from copy import deepcopy


def main():
    """Runs the game"""
    width, height = take_dimensions()
    board = make_board(width, height)
    cell_size = len(board[0][0])

    print('Enter the knight\'s starting position: ', end='')
    position = take_position(board)
    board = make_move(board, cell_size, position)
    knight_position = position
    pos_moves = find_possible_moves(board, knight_position)
    pos_moves_num = find_possible_move_num(board, pos_moves)
    display_board(mark_possible_moves(board, cell_size, pos_moves, pos_moves_num), cell_size)

    completed = None
    moves_made = 1
    while pos_moves:
        print('Enter your next move: ', end='')
        position = take_position(board)
        if position not in pos_moves:
            print('Invalid position!')
            continue
        make_move(board, cell_size, position, knight_position)
        moves_made += 1
        knight_position = position # assign new current knight_position
        pos_moves = find_possible_moves(board, knight_position)
        pos_moves_num = find_possible_move_num(board, pos_moves)
        display_board(mark_possible_moves(board, cell_size, pos_moves, pos_moves_num), cell_size)
        completed = is_tour_completed(board, pos_moves)

    if completed:
        print('What a great tour! Congratulations!')
    else:
        print('No more possible moves!')
        print(f'Your knight visited {moves_made} squares!')


def take_dimensions() -> tuple:
    """Return the dimensions to construct the board"""
    while True:
        message = 'Invalid dimensions!\n'
        dimensions = input('Enter your board dimensions: ').split()
        if len(dimensions) != 2:
            print(message)
            continue

        check = all([dimension.isdigit() for dimension in dimensions])
        if not check:
            print(message)
            continue

        width, height = int(dimensions[0]), int(dimensions[1])
        if width < 1 or height < 1:
            print(message)
            continue

        return width, height


def make_board(width: int, height: int) -> list:
    """Return the board with the given dimensions"""
    cell_number = width * height
    cell = '_' * len(str(cell_number))
    board = [[cell for _ in range(width)] for _ in range(height)]
    return board


def take_position(board: list) -> tuple or bool:
    """Return the coordinates of the move"""
    while True:
        points = input().split()
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


def make_move(board: list, cell_size: int, new_position: tuple, old_position: tuple = None) -> list:
    """Return the chess board with the inserted knight's position.
    Mark new position with 'X' and visited one (old_position) with the '*'.
    If there are no visited squares (start of the game) leave out the old_position"""
    if old_position:
        old_inner, old_outer = into_index(board, old_position)
        board[old_outer][old_inner] = '*'.rjust(cell_size)
    new_inner, new_outer = into_index(board, new_position)
    board[new_outer][new_inner] = 'X'.rjust(cell_size)
    return board


def mark_possible_moves(board: list, cell_size: int, moves: list, move_num: list) -> list:
    """Return the chess board with the number of possible moves from the given position marked"""
    copy_board = deepcopy(board)
    for move, number in zip(moves, move_num):
        inner, outer = into_index(board, move)
        copy_board[outer][inner] = str(number).rjust(cell_size)
    return copy_board


def find_possible_moves(board: list, starting_point: tuple) -> list:
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

        inner, outer = into_index(board, (pos_row, pos_column))
        if 'X' in board[outer][inner] or '*' in board[outer][inner]:
            continue
        moves.append((pos_row, pos_column))

    return moves


def find_possible_move_num(board: list, possible_moves: list) -> list:
    """Return the list of possible moves for each of the given positions"""
    possible_moves_num = [len(find_possible_moves(board, move)) for move in possible_moves]
    return possible_moves_num


def is_tour_completed(board: list, possible_moves: list) -> bool:
    """Return whether the tour has been completed successfully"""
    free_cells_num = sum(('_' in cell for row in board for cell in row))
    if free_cells_num == 0 and len(possible_moves) == 0:
        return True
    else:
        return False


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
    print('\n')


if __name__ == '__main__':
    main()
