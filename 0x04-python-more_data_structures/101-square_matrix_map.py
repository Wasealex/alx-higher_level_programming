#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda r: list(map(lambda element: element**2, r)), matrix))
