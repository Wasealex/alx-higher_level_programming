#!/usr/bin/python3
def uppercase(str):
    output = ""
    for i in str:
        if (ord('a') <= ord(i) and ord(i) <= ord('z')):
            upper_case = chr(ord(i) - 32)
            output = output + upper_case
        else:
            output = output + i
    print("{}".format(output))
