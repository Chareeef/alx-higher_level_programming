#!/usr/bin/python3
"""
Implementation of matrix_divided
Tested with tests/2-matrix_divided.txt
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div
    and store the results in a new matrix

    Returns: The new matrix
    """

    # Error messages:
    error_matrix_types = "matrix must be a matrix (list of lists) "
    error_matrix_types += "of integers/floats"

    error_different_size = "Each row of the matrix must have the same size"

    error_div_type = "div must be a number"

    error_division_zero = "division by zero"

    # Check type of matrix and its elements:
    if not isinstance(matrix, list):
        raise TypeError(error_matrix_types)
    if len(matrix) < 1:
        raise TypeError(error_matrix_types)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_matrix_types)
        if len(row) < 1:
            raise TypeError(error_matrix_types)
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError(error_matrix_types)

    # Check that each row in matrix has the same size:
    first_row_length = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_length:
            raise TypeError(error_different_size)

    # Check if div is a number (int/float), and is not zero:
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError(error_div_type)
    if div == 0:
        raise ZeroDivisionError(error_division_zero)

    # Create and populate the new matrix:
    quotient_matrix = []

    for row in matrix:
        quotient_row = []
        for n in row:
            quotient = n / div
            quotient_row.append(round(quotient, 2))
        quotient_matrix.append(quotient_row)

    # Return the new matrix populated with quotients:
    return quotient_matrix


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/2-matrix_divided.txt")
