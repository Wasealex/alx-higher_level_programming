#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > len(my_list):
        return None
    for i in range(len(my_list)):
        if i == idx:
            return my_list[i]
