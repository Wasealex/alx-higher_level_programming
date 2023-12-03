#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    else:
        new_list = my_list[:]
        for idx in new_list:
            if new_list[idx] % 2 == 0:
                new_list[idx] = True
            else:
                new_list[idx] = False
        return new_list
