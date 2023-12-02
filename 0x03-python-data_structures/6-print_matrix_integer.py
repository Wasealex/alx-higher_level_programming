#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for rows in matrix:
            for idx in range(len(rows)):
                print("{:d}".format(rows[idx]), end='')
                if 0 <= idx < len(rows):
                    print(" ", end='')
            print("")
