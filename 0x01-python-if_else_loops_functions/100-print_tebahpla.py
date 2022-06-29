#!/usr/bin/python3
newstr = ""
i = 122
while i != 96:
    if i % 2 != 0:
        newstr += chr(i - 32)
    else:
        newstr += chr(i)
    i -= 1
print("{}".format(newstr), end="")
