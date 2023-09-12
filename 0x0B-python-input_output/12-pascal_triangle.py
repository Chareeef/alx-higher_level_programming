#!/usr/bin/python3
'''This module contains pascal_triangle() function implementation'''


def pascal_triangle(n):
    '''Returns a list of lists of integers
    representing the Pascal’s triangle of n rows

    Arguments:
        n (int): the number of rows

    Returns:
        Pascal's triangle (list of lists)
    '''

    if n < 1:
        return []

    pt = [[1]]  # primary Pascal's triangle

    for r in range(1, n):  # For each row after the first one
        current_row = []

        for c in range(0, r + 1):  # Each row r has r + 1 columns
            if c == 0 or c == r:  # First and last columns contain always 1
                n = 1
            else:  # For middle columns
                n = pt[r - 1][c] + pt[r - 1][c - 1]

            # Update the current row:
            current_row.append(n)

        # Add the new row to Pascal's triangle
        pt.append(current_row)

    # Return the Pascal's triangle
    return pt


def print_pascal(n):
    '''Prints a Pascal's triangle of n rows

    Arguments:
        n (int): the number of rows
    '''

    pt = pascal_triangle(n)

    for row in pt:
        print("[{}]".format(','.join([str(x) for x in row])))


if __name__ == '__main__':
    print('\n\t*******\n')
    print_pascal(-2)
    print('\n\t*******\n')
    print_pascal(0)
    print('\n\t*******\n')
    print_pascal(1)
    print('\n\t*******\n')
    print_pascal(2)
    print('\n\t*******\n')
    print_pascal(3)
    print('\n\t*******\n')
    print_pascal(4)
    print('\n\t*******\n')
    print_pascal(8)
