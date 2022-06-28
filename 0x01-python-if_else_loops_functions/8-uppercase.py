#!/usr/bin/python3
def uppercase(str):
    a = 0
    newstr = ""
    while a != len(str):
        if ord(str[a]) >= 97 and ord(str[a]) <= 122:
            newstr += chr(ord(str[a]) - 32)
        else:
            newstr += str[a]
            a += 1
            print("{}".format(newstr))
