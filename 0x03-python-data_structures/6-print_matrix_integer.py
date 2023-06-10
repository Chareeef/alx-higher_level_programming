#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return

    col_length = len(matrix)
    if col_length == 0:
        print()
        return

    row_length = len(matrix[0])
    if row_length == 0:
        print()
        return

    for i in range(col_length):
        for j in range(row_length - 1):
            print('{}'.format(matrix[i][j]), end=' ')
        if row_length == 1:
            j = -1
        print('{}'.format(matrix[i][j + 1]))
