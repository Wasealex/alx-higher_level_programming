#!/usr/bin/python3
"""contains one class MyList()
"""


class MyList(list):
    """a subclass of list that inherits
    """

    def print_sorted(self):
        """prints sorted list
        """
        print(sorted(self))
