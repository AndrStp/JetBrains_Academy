from copy import deepcopy
from typing import List


def solve(board: list, start: tuple, visited: int) -> List[list] or False:
    """Returns the chess-board with order of moves marked or False if no solution exists"""
    board_size = len(board) * len(board[0])

    possible_moves = find_possible_moves(board, start)
    pos_moves_num = find_possible_move_num(board, possible_moves)
    move_num_pairs = [(move, move_num) for move, move_num in zip(possible_moves, pos_moves_num)]
    sorted_move_num_pairs = sorted(move_num_pairs, key=lambda moves_num: moves_num[1])

    cell_size = len(board[0][0])
    for move_num_pair in sorted_move_num_pairs:
        move = move_num_pair[0]
        inner, outer = into_index(board, move)
        board[outer][inner] = str(visited).rjust(cell_size)
        if visited == board_size:
            return board
        if solve(board, move, visited+1):
            return board
    return False


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


def take_position(board: list) -> tuple:
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


def take_decision() -> str:
    """Return the user decision: 'y' or 'n'"""
    while True:
        print('Do you want to try the puzzle? (y/n): ', end='')
        option = input().lower()
        if option not in ('y', 'n'):
            print('Invalid option')
            continue
        return option


def make_board(width: int, height: int) -> List[list]:
    """Return the board with the given dimensions"""
    cell_number = width * height
    cell = '_' * len(str(cell_number))
    board = [[cell for _ in range(width)] for _ in range(height)]
    return board


def into_index(board: list, coordinates: tuple) -> tuple:
    """Return the list indexes for internal representation"""
    inner, outer = coordinates[0] - 1, abs(coordinates[1] - len(board))
    return inner, outer


def make_move(board: list, filler: str, new_position: tuple, old_position: tuple = None) -> List[list]:
    """Return the chess board with the inserted knight's position.
    Mark new position with 'X' and visited one (old_position) with the '*'.
    If there are no visited squares (start of the game) leave out the old_position"""
    cell_size = len(board[0][0])
    if old_position:
        old_inner, old_outer = into_index(board, old_position)
        board[old_outer][old_inner] = '*'.rjust(cell_size)
    new_inner, new_outer = into_index(board, new_position)
    board[new_outer][new_inner] = filler.rjust(cell_size)
    return board


def mark_possible_moves(board: list, moves: list, move_num: list) -> List[list]:
    """Return the chess board with the number of possible moves from the given position marked"""
    cell_size = len(board[0][0])
    copy_board = deepcopy(board)
    for move, number in zip(moves, move_num):
        inner, outer = into_index(board, move)
        copy_board[outer][inner] = str(number).rjust(cell_size)
    return copy_board


def find_possible_moves(board: list, knight_position: tuple) -> List[tuple]:
    """Returns the list of valid moves for the given knight position"""
    row, column = knight_position
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
        if '_' not in board[outer][inner]:
            continue
        moves.append((pos_row, pos_column))

    return moves


def find_possible_move_num(board: list, possible_moves: list) -> List[int]:
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


def display_board(board: list) -> None:
    """Displays the chess board (i.e. start counting from 1 to 8 and
    from left to right and from bottom to top"""
    cell_size = len(board[0][0])
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
