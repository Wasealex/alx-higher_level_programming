#!/usr/bin/python3
"""
    This is a "2-matrix_divided" module

    contains one function matrix_divided()
    returns a new matrix that is divided by a given number
"""


def matrix_divided(matrix, div):
    """matrix_divided function takes list of lists and divisor and
       returns a new matrix(list of lists) after division
       args:
            matrix(list of lists) = the first parameter
                  should be a list which contains lists of equal sizes
                  sub list must contain only intigers and not empty
            div(int) = the second parameter
                  should be an non zero integer value
       returns:
            new_matrix
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
