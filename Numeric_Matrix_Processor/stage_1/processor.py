from typing import List, Optional


def main():
    row, column = map(int, input().split())
    m1 = make_matrix(row)
    row, column = map(int, input().split())
    m2 = make_matrix(row)
    m_sum = add_matrices(m1, m2)
    if m_sum:
        display_matrix(m_sum)
    else:
        print('ERROR')


def make_matrix(row: int) -> List[list]:
    """Return the matrix with given n rows"""
    return [list(map(int, input().split())) for _ in range(row)]


def add_matrices(matrix_1: List[list], matrix_2: List[list]) -> Optional[List[list]]:
    """Return the matrix by adding two matrices"""
    if not check_matrices(matrix_1, matrix_2):
        return None

    matrix = []
    for row_1, row_2 in zip(matrix_1, matrix_2):
        matrix_row = []
        for cell_1, cell_2 in zip(row_1, row_2):
            matrix_row.append(cell_1 + cell_2)
        matrix.append(matrix_row)
    return matrix


def check_matrices(matrix_1: List[list], matrix_2: List[list]) -> bool:
    """Returns whether the given matrices are of equal size"""
    matrix_1_row_num, matrix_1_col_num = len(matrix_1), len(matrix_1[0])
    matrix_2_row_num, matrix_2_col_num = len(matrix_2), len(matrix_2[0])
    if (matrix_1_row_num, matrix_1_col_num) != (matrix_2_row_num, matrix_2_col_num):
        return False
    return True


def display_matrix(matrix: List[list]) -> None:
    """Displays the matrix"""
    for row in matrix:
        for cell in row:
            print(cell, end=' ')
        print()


if __name__ == '__main__':
    main()
