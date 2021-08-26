import chess_methods as methods
from copy import deepcopy


def main():
    """Runs the game"""
    width, height = methods.take_dimensions()
    board = methods.make_board(width, height)

    print('Enter the knight\'s starting position: ', end='')
    knight_position = methods.take_position(board)
    knight = 'X'

    decision = methods.take_decision()
    if decision == 'n':
        knight = str(1)
        board = methods.make_move(board, knight, knight_position)
        board_copy = deepcopy(board)
        solution = methods.solve(board_copy, knight_position, 2)
        if not solution:
            print('No solution exists!')

        else:
            print('Here\'s the solution!')
            methods.display_board(solution)

    else:
        board = methods.make_move(board, knight, knight_position)
        board_copy = deepcopy(board)
        solution = methods.solve(board_copy, knight_position, 2)
        if not solution:
            print('No solution exists!')
            quit()

        board = methods.make_move(board, knight, knight_position)
        pos_moves = methods.find_possible_moves(board, knight_position)
        pos_moves_num = methods.find_possible_move_num(board, pos_moves)
        methods.display_board(methods.mark_possible_moves(board, pos_moves, pos_moves_num))

        completed = None
        moves_made = 1
        while pos_moves:
            print('Enter your next move: ', end='')
            new_position = methods.take_position(board)

            if new_position not in pos_moves:
                print('Invalid position!', end='')
                continue

            methods.make_move(board, knight, new_position, knight_position)
            moves_made += 1
            knight_position = new_position
            pos_moves = methods.find_possible_moves(board, knight_position)
            pos_moves_num = methods.find_possible_move_num(board, pos_moves)
            methods.display_board(methods.mark_possible_moves(board, pos_moves, pos_moves_num))
            completed = methods.is_tour_completed(board, pos_moves)

        if completed:
            print('What a great tour! Congratulations!')
        else:
            print('No more possible moves!')
            print(f'Your knight visited {moves_made} squares!')


if __name__ == '__main__':
    main()
