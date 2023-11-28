#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if (i != j and j > i and (i != 8 or j != 9)):
            print("{}{}".format(i, j), end=', ')
print("89")
