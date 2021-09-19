from __future__ import annotations
from typing import List, Optional


class Matrix:
    """A matrix class"""

    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column
        self.matrix: List[list] = [[0 for _ in range(self.column)] for _ in range(self.row)]

    @classmethod
    def add_matrices(cls, matrix_1: Matrix, matrix_2: Matrix) -> Optional[Matrix]:
        """Return the matrix by adding two matrices"""
        if not Matrix.check_add_matrices(matrix_1, matrix_2):
            return None

        new_matrix = Matrix(matrix_1.row, matrix_1.column)
        for i in range(matrix_1.row):
            for j in range(matrix_1.column):
                new_matrix.matrix[i][j] = matrix_1.matrix[i][j] + matrix_2.matrix[i][j]
        return new_matrix

    @classmethod
    def check_add_matrices(cls, matrix_1: Matrix, matrix_2: Matrix) -> bool:
        """Returns True of False whether the given matrices are of equal size"""
        if (matrix_1.row, matrix_1.column) != (matrix_2.row, matrix_2.column):
            return False
        return True

    @classmethod
    def check_mult_matrices(cls, matrix_1: Matrix, matrix_2: Matrix) -> bool:
        """Returns True if the number of row in the matrix_1 equals to
        the number of columns in the matrix_2. Returns False otherwise"""
        if matrix_1.column != matrix_2.row:
            return False
        return True

    @classmethod
    def multiply_matrices(cls, matrix_1: Matrix, matrix_2: Matrix) -> Optional[Matrix]:
        """Return the matrix by multiplying matrix_1 by matrix_2"""
        if not Matrix.check_mult_matrices(matrix_1, matrix_2):
            return None

        new_matrix = Matrix(matrix_1.row, matrix_2.column)
        for i in range(matrix_1.row):
            for j in range(matrix_2.column):
                for k in range(matrix_2.row):
                    new_matrix.matrix[i][j] += matrix_1.matrix[i][k] * matrix_2.matrix[k][j]
        return new_matrix

    def fill_matrix(self) -> None:
        """Fill the matrix with values"""
        self.matrix = [[int(n) if n.isdigit() else float(n)
                        for n in input().split()]
                       for _ in range(self.row)]

    def multiply_matrix(self, constant):
        """Return the result of multiplying a matrix by a constant"""
        self.matrix = [[cell * constant for cell in row] for row in self.matrix]

    # helper method
    @staticmethod
    def display_matrix(matrix: Matrix):
        for row in matrix.matrix:
            for el in row:
                print(el, end=' ')
            print()
        print()
