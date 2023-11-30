#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no_of_argument = len(sys.argv)
    sum = 0
    for i in range(1, no_of_argument):
        sum = sum + int(sys.argv[i])
    print("{:d}".format(sum))
