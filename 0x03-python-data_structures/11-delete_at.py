#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (0 <= idx < len(my_list) and my_list is not None):
        del my_list[idx]
        return my_list
    else:
        return my_list
