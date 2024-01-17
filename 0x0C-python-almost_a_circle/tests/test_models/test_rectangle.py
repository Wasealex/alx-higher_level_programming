#!/usr/bin/python3
"""tests for rectangle methods
"""
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class
    """
    def test_two_args(self):
        r1 = Rectangle(5, 10)
        r2 = Rectangle(10, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(2, 4, 6, 8)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_two_args_print(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(str(r1), "[Rectangle] (12) 0/0 - 1/2")

    def test_six_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 1, 2, 3)

if __name__ == '__main__':
    unittest.main()
