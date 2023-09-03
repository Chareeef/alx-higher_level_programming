#!/usr/bin/python3
"""
Implementation of 101-lazy_matrix_mul
Tested with tests/101-lazy_matrix_mul.txt
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using numpy

    Args:
        m_a (matrix: list of lists)
        m_b (matrix: list of lists)

    Returns: The product matrix
    """

    # Let's be lazyyyy:
    return np.array(m_a) @ np.array(m_b)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/101-lazy_matrix_mul.txt")
