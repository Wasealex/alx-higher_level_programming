#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            newstr += chr(ord(c) - 32)
        else:
            newstr += c
            print("{}".format(newstr))
