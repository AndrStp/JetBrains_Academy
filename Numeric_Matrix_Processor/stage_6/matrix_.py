from __future__ import annotations
from typing import List, Optional, Union
from copy import deepcopy
import numpy as np


class Matrix:
    """A matrix class"""

    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column
        self.matrix: List[list] = [[0 for _ in range(self.column)] for _ in range(self.row)]
        self.determinant = None

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

    @classmethod
    def transpose_matrix(cls, matrix: Matrix, option: int) -> Matrix:
        """Return the transposed matrix. Matrix transposition
        could be done in four different ways (types).
        Applicable only to square matrices."""
        types = {1: 'main', 2: 'side',  3: 'vertical', 4: 'horizontal'}
        type_ = types.get(option)

        new_matrix = Matrix(matrix.row, matrix.column)

        if type_ == 'main':
            new_matrix.matrix = [[matrix.matrix[j][i] for j in range(matrix.column)]
                                 for i in range(matrix.row)]

        if type_ == 'side':
            new_matrix.matrix = [[matrix.matrix[abs(matrix.column - 1 - j)][abs(matrix.row - 1 - i)]
                                  for j in range(matrix.column)]
                                 for i in range(matrix.row)]

        if type_ == 'vertical':
            new_matrix.matrix = [[matrix.matrix[i][matrix.column - 1 - j] for j in range(matrix.column)]
                                 for i in range(matrix.row)]

        if type_ == 'horizontal':
            new_matrix.matrix = [[matrix.matrix[-1 - i][j] for j in range(matrix.column)]
                                 for i in range(matrix.row)]
        return new_matrix

    @classmethod
    def inverse_matrix(cls, matrix: Matrix) -> Optional[Matrix]:
        """Return the inversed matrix if possible otherwise None
        aka I gave up, maybe another time I will complete it :)"""
        determinant = matrix.calc_determinant()
        if not determinant:
            return None

        # magic function in action :)
        inversed_numpy = np.linalg.inv(matrix.matrix)

        # convert to Matrix class instance
        new_matrix = Matrix(matrix.row, matrix.column)
        for i in range(new_matrix.row):
            for j in range(new_matrix.column):
                value = np.round(inversed_numpy[i][j], 3)
                if str(value) == '0.0':
                    new_matrix.matrix[i][j] = 0
                else:
                    new_matrix.matrix[i][j] = value

        return new_matrix

    def fill_matrix(self) -> None:
        """Fill the matrix with values"""

        self.matrix = [[int(n) if n.isdigit() else float(n)
                        for n in input().split()]
                       for _ in range(self.row)]

    def multiply_matrix(self, constant: Union[int, float]) -> None:
        """Return the result of multiplying a matrix by a constant"""

        self.matrix = [[cell * constant for cell in row] for row in self.matrix]

    def calc_determinant(self) -> float:
        """Returns the determinant of the given matrix"""
        n = len(self.matrix)
        temp_matrix = deepcopy(self.matrix)

        for fd in range(n):
            for i in range(fd+1, n):
                if temp_matrix[fd][fd] == 0:
                    temp_matrix[fd][fd] = 1.0e-10

                cr_scalar = temp_matrix[i][fd] / temp_matrix[fd][fd]
                for j in range(n):
                    temp_matrix[i][j] = temp_matrix[i][j] - cr_scalar * temp_matrix[fd][j]

        product = 1.0
        for i in range(n):
            product *= temp_matrix[i][i]

        return product
