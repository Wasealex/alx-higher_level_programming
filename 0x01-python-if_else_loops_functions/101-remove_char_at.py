#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        print("{}".format(str))
    else:
        new_string = ""
        for i in range(len(str)):
            if i != n:
                new_string = new_string + str[i]
        print("{}".format(new_string))
