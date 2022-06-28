#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if a == 8 and b == 9:
            print("89")
            break
        else:
            if a != b and b > a:
                print("{}{}, ".format(a, b), end="")
