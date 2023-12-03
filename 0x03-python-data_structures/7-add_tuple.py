#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (tuple_a or tuple_b is ()):
        tuple_a = tuple_a + (0, 0)
        tuple_b = tuple_b + (0, 0)
    if (tuple_a[0] or tuple_a[1] or tuple_b[0] or tuple_b[1] is ()):
        tiple_a = tuple_a + (0, 0)
        tuple_b = tuple_b + (0, 0)
    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    return (a, b)
