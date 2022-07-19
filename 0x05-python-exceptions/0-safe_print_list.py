#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while(x > 0):
            print("{}".format(my_list[i]), end="")
            x -= 1
            i += 1
    except IndexError:
        pass
    print()
    return i
