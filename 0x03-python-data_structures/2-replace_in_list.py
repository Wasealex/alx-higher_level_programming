#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        for i in range(len(my_list)):
            my_list[idx] = element
    return my_list
