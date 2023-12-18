#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    no_ele = 0
    for element in my_list:
        try:
            count += 1
            if (x >= count):
                no_ele += 1
                print("{:d}".format(element), end='')
        except (ValueError, TypeError):
            continue
    print()
    return (no_ele)
