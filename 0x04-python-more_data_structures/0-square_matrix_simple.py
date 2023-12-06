#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    new_matrix = []
    for rows in matrix:
        new_row = []
        for element in rows:
            new = element ** 2
            new_row.append(new)
        new_matrix.append(new_row)
    return new_matrix
