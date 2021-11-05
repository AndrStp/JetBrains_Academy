
from __future__ import annotations
import numpy as np
# from collections import deque


class Grid:
    """Grid object and related functionality"""
    FILLING = '-'

    def __init__(self,
                 piece: Piece,
                 width: int = 10,
                 height: int = 20) -> None:
        self.width = width
        self.height = height
        # 1-d np-array
        self.grid = np.array([Grid.FILLING] * self.width * self.height)
        self.piece = piece

    def display_grid(self) -> None:
        temp_grid = [' '.join(self.grid[self.width * i:self.width * i + self.width])
                     for i in range(self.height)]
        print(*temp_grid, sep='\n')
        print()

    def insert_piece(self) -> None:
        """Insert Piece's coordinates to grid"""
        self.grid[:] = Grid.FILLING
        for coordinate in self.piece.forms[self.piece.index]:
            self.grid[coordinate] = 0


class Piece:
    """Piece object from which pieces inherit"""
    def __init__(self):
        self.forms: np.array = None
        self.rotation = 0
        self.index = 0

    def down(self) -> None:
        self.forms += 10

    def left(self) -> None:
        self.forms += -1
        self.down()

    def right(self) -> None:
        self.forms += 1
        self.down()

    def rotate(self) -> None:
        self.rotation += 1
        self.index = self.rotation % len(self.forms)
        self.down()


class PieceO(Piece):
    def __init__(self):
        super().__init__()
        self.forms = np.array([[4, 14, 15, 5]])


class PieceI(Piece):
    def __init__(self):
        super().__init__()
        self.forms = np.array([[4, 14, 24, 34],
                               [3, 4, 5, 6]])


class PieceS(Piece):
    def __init__(self):
        super().__init__()
        self.forms = np.array([[5, 4, 14, 13],
                               [4, 14, 15, 25]])


class PieceZ(Piece):
    def __init__(self):
        super().__init__()
        self.forms = np.array([[4, 5, 15, 16],
                               [5, 15, 14, 24]])


class PieceL(Piece):
    def __init__(self):
        super().__init__()
        self.forms = np.array([[4, 14, 24, 25],
                               [5, 15, 14, 13],
                               [4, 5, 15, 25],
                               [6, 5, 4, 14]])


class PieceJ(Piece):
    def __init__(self):
        super().__init__()
        self.forms = np.array([[5, 15, 25, 24],
                               [15, 5, 4, 3],
                               [5, 4, 14, 24],
                               [4, 14, 15, 16]])


class PieceT(Piece):
    def __init__(self):
        super().__init__()
        self.forms = np.array([[4, 14, 24, 15],
                               [4, 13, 14, 15],
                               [5, 15, 25, 14],
                               [4, 5, 6, 15]])


if __name__ == '__main__':

    pieces = {
        'O': PieceO(),
        'I': PieceI(),
        'S': PieceS(),
        'Z': PieceZ(),
        'L': PieceL(),
        'J': PieceJ(),
        'T': PieceT()
    }
    for piece_ in pieces:
        my_piece = pieces.get(piece_)
        game = Grid(my_piece)
        game.insert_piece()
        print('NEW PIECE'.center(16, '-'))
        game.display_grid()

