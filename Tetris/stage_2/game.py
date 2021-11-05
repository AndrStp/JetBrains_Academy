
import objects


def main():

    pieces = {
        'O': objects.PieceO(),
        'I': objects.PieceI(),
        'S': objects.PieceS(),
        'Z': objects.PieceZ(),
        'L': objects.PieceL(),
        'J': objects.PieceJ(),
        'T': objects.PieceT()
    }

    choice, width, height = take_args()
    game = objects.Grid(pieces.get(choice), width, height)
    game.display_grid()
    game.insert_piece()
    game.display_grid()

    commands = {'down', 'left', 'right', 'rotate', 'exit'}

    while True:
        while (command := input()) in commands:
            if command == 'exit':
                exit()
            game.piece.__getattribute__(command)()
            game.insert_piece()
            game.display_grid()
        else:
            print('Invalid command. Use:', ', '.join(commands))


def take_args() -> tuple[str, int, int]:
    """Read and return args from the user
    tuple of (piece, width and height of the grid"""
    piece = input().upper()
    width, height = map(int, input().split())
    return piece, width, height


if __name__ == '__main__':
    main()
