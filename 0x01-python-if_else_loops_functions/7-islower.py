#!/usr/bin/python3
def islower(c):
    asc = ord(c)
    if asc >= 97 and asc <= 122:
        return True
    else:
        return False
