#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    no_of_arguments = len(sys.argv)
    if no_of_arguments <= 1:
        print("0 arguments.")
    else:
        if no_of_arguments == 2:
            print("{:d} argument:".format(no_of_arguments - 1))
            print("1: {}".format(sys.argv[1]))
        else:
            print("{:d} arguments:".format(no_of_arguments - 1))
            for i in range(1, no_of_arguments):
                print("{:d}: {}".format(i, sys.argv[i]))
