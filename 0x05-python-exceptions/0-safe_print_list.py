#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        no_ele = 0
        for elements in my_list:
            count += 1
            if (x >= count):
                no_ele += 1
                print(elements, end='')
        print()
        return (no_ele)
    except IndexError:
        pass
