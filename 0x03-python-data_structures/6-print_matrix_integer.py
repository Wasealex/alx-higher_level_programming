#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for rows in matrix:
            for idx in range(len(rows)):
                print("{:d}".format(rows[idx]), end='')
                if idx != len(rows) - 1:
                    print(" ", end='')
            print("")
