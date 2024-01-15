#!/usr/bin/python3
"""tests for rectangle methods
"""
from models.rectangle import Rectangle
import unittest


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class
    """

    def test_two_args(self):
        r1 = Rectangle(5, 10)
        r2 = Rectangle(10, 5)
        self.assertEqual(r1.id, r2.id - 1)

if __name__ == '__main__':
    unittest.main()
