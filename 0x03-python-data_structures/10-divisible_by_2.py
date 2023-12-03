#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return
    else:
        new_list = []
        for element in my_list:
            if element % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
