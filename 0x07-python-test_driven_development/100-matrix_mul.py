#!/usr/bin/python3
"""
Implementation of 0-matrix_mul
Tested with tests/0-matrix_mul.txt
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices

    Args:
        m_a (matrix: list of lists)
        m_b (matrix: list of lists)

    Returns: The product matrix
    """

    # if m_a or m_b is not a list:
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # if m_a or m_b is not a list of lists:
    for item in m_a:
        if not isinstance(item, list):
            raise TypeError(
                "m_a must be a list of lists or m_b must be a list of lists")
    for item in m_b:
        if not isinstance(item, list):
            raise TypeError(
                "m_a must be a list of lists or m_b must be a list of lists")

    # if m_a or m_b is empty (it means: = [] or = [[], [], ...]):
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    empty = True
    for item in m_a:
        if len(item) > 0:
            empty = False
    if empty:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    empty = True
    for item in m_b:
        if len(item) > 0:
            empty = False
    if empty:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # if one element of those list of lists is not an integer or a float:
    for row in m_a:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                        "m_a should contain only integers or floats" +
                        " or m_b should contain only integers or floats")
    for row in m_b:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                        "m_a should contain only integers or floats" +
                        " or m_b should contain only integers or floats")

    # if m_a or m_b ‘rows’ do not have the same size:
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError(
                    "each row of m_a must be of the same size " +
                    "or each row of m_b must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError(
                    "each row of m_a must be of the same size " +
                    "or each row of m_b must be of the same size")

    # If m_a and m_b can’t be multiplied ->
    #       number of columns of m_a != number of rows in m_b:
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # And now... Let's multiply matrices !!
    matrix_product = []

    rows_a, rows_b = len(m_a), len(m_b)
    cols_a, cols_b = len(m_a[0]), len(m_b[0])

    m_a_row, m_a_col = 0, 0
    m_b_row, m_b_col = 0, 0

    while m_a_row < rows_a:

        row_product = []

        while m_b_col < cols_b:

            result = 0
            while m_a_col < cols_a:
                result += m_a[m_a_row][m_a_col] * m_b[m_b_row][m_b_col]
                m_a_col += 1
                m_b_row += 1

            row_product.append(result)
            m_b_col += 1
            m_a_col, m_b_row = 0, 0

        matrix_product.append(row_product)
        m_a_row += 1
        m_b_col = 0

    return matrix_product


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/100-matrix_mul.txt")
