#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for idx in range(x):
        try:
            count += 1
            print("{:d}".format(my_list[idx]), end='')
        except (ValueError, TypeError):
            continue
    print()
    return (count)
