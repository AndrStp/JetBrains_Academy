from __future__ import annotations
import matrix_ as M


def main():
    while True:
        menu = ['1. Add matrices',
                '2. Multiply matrix by a constant',
                '3. Multiply matrices',
                '4. Transpose matrix',
                '5. Calculate a determinant',
                '0. Exit']
        print(*menu, sep='\n')

        choice = int(input('Your choice: '))
        if choice == 1:
            row, column = map(int, input('Enter size of first matrix: ').split())
            print('Enter first matrix:')
            matrix_1 = create_matrix(row, column)

            row, column = map(int, input('Enter size of second matrix: ').split())
            print('Enter second matrix:')
            matrix_2 = create_matrix(row, column)

            new_matrix = M.Matrix.add_matrices(matrix_1, matrix_2)
            print('The result is:')
            if new_matrix:
                display_matrix(new_matrix)
            else:
                print('The operation cannot be performed.')

        if choice == 2:
            row, column = map(int, input('Enter size of matrix: ').split())
            print('Enter matrix:')
            matrix = create_matrix(row, column)

            constant = float(input('Enter constant: '))
            matrix.multiply_matrix(constant)

            print('The result is:')
            display_matrix(matrix)

        if choice == 3:
            row, column = map(int, input('Enter size of first matrix: ').split())
            print('Enter first matrix:')
            matrix_1 = create_matrix(row, column)

            row, column = map(int, input('Enter size of second matrix: ').split())
            print('Enter second matrix:')
            matrix_2 = create_matrix(row, column)

            new_matrix = M.Matrix.multiply_matrices(matrix_1, matrix_2)
            print('The result is:')
            if new_matrix:
                display_matrix(new_matrix)
            else:
                print('The operation cannot be performed.')

        if choice == 4:
            options = ['1. Main diagonal',
                       '2. Side diagonal',
                       '3. Vertical line',
                       '4. Horizontal line']
            print(*options, sep='\n')
            option = int(input('Your choice: '))

            row, column = map(int, input('Enter matrix size: ').split())
            print('Enter matrix:')
            matrix = create_matrix(row, column)

            new_matrix = M.Matrix.transpose_matrix(matrix, option)
            print('The result is:')
            display_matrix(new_matrix)

        if choice == 5:
            row, column = map(int, input('Enter matrix size: ').split())
            print('Enter matrix:')
            matrix = create_matrix(row, column)

            print('The result is:')
            print(matrix.calc_determinant())

        print()
        if choice == 0:
            break


def create_matrix(row: int, column: int) -> M.Matrix:
    """Return a Matrix object"""
    matrix = M.Matrix(row, column)
    matrix.fill_matrix()
    return matrix


def display_matrix(matrix: M.Matrix) -> None:
    """Displays the matrix"""
    for row in matrix.matrix:
        for cell in row:
            print(cell, end=' ')
        print()


if __name__ == '__main__':
    main()
