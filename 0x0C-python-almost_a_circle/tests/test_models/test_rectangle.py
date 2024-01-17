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

    def test_two_args_print(self):
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (13) 3/0 - 1/2")

    def test_two_args_print(self):
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (14) 3/4 - 1/2")

    def test_two_args_print(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 1/2")

    def test_six_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 1, 2, 3)

class TestRectangleErrors(unittest.TestCase):

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3", 4)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(5, 3, 1, -1)

    def test_area_1(self):
        r1 = Rectangle(2, 4)
        self.assertEqual(8, r1.area())

    def test_area_2(self):
        r1 = Rectangle(5, 10, 1, 5, 10)
        self.assertEqual(50, r1.area())

if __name__ == '__main__':
    unittest.main()
