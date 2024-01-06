#!/usr/bin/python3
"""This module is "4-print_square"

   it has one function, print_square()
   prints '#' for a given positive intiger size
"""


def print_square(size):
    """
    function print_square takes one argument and prints out
    '#' square shaped of a given size

    Args:
         size(int) = the only parameter
             must be a positive integer

    Returns:
            None
    Output:
           '#' for size=1
           '##
            ##' for size=2
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for rows in range(size):
        for col in range(size):
            print('#', end='')
        print()
