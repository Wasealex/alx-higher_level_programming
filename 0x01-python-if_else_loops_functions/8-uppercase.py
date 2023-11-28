#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord('a') <= ord(i) and ord(i) <= ord('z')):
            upper_case = chr(ord(i) - 32)
            print("{}".format(upper_case), end='')
        else:
            print("{}".format(i), end='')
    print("")
