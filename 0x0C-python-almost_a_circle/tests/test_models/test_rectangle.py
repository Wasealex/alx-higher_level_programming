#!/usr/bin/python3
"""tests for rectangle methods
"""
from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys
from io import StringIO


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
    """testing different values for Rectangle
    """
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

class TestRectangleArea(unittest.TestCase):
    """testing area() method of class Rectangle
    """
    def test_area_1(self):
        r1 = Rectangle(2, 4)
        self.assertEqual(8, r1.area())

    def test_area_2(self):
        r1 = Rectangle(5, 10, 1, 5, 10)
        self.assertEqual(50, r1.area())

class TestRectangleDisplay(unittest.TestCase):
    """ unittest for testing the display() method of Rectangle
    """
    @staticmethod
    def assert_printed(expected, test):
        output = StringIO()
        sys.stdout = output
        test()
        out = output.getvalue()
        sys.stdout = sys.__stdout__
        assert expected == out

    def test_display_width_height(self):
        r1 = Rectangle(3, 3, 0, 0, 0)
        self.assert_printed("###\n###\n###\n", r1.display)

    def test_display_width_height_x(self):
        r = Rectangle(3, 2, 1, 0, 1)
        self.assert_printed(" ###\n ###\n", r.display)

    def test_display_width_height_y(self):
        r = Rectangle(4, 5, 0, 1, 0)
        o = "\n####\n####\n####\n####\n####\n"
        self.assert_printed(o, r.display)

    def test_display_width_height_x_y(self):
        r = Rectangle(2, 4, 3, 2, 0)
        o = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assert_printed(o, r.display)

class TestRectangle_to_dictionary(unittest.TestCase):
    """testing to_dictionary() method of the Rectangle"""

    def test_to_dictionary_output(self):
        r = Rectangle(1, 2, 3, 4, 5)
        expected = {'width': 1, 'height': 2, 'x': 3, 'y': 4, 'id': 5}
        self.assertDictEqual(expected, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

class TestRectangle_update_args(unittest.TestCase):
    """testing update() method of the Rectangle"""

    def test_update_args_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(15)
        self.assertEqual("[Rectangle] (15) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(15, 2)
        self.assertEqual("[Rectangle] (15) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(15, 2, 3)
        self.assertEqual("[Rectangle] (15) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(15, 2, 3, 4)
        self.assertEqual("[Rectangle] (15) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(15, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (15) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(15, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (15) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(15, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 15)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(15, "2")

    def test_update_args_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(15, 0)

    def test_update_args_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(15, -5)

    def test_update_args_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(15, 2, "invalid")

    def test_update_args_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(15, 1, 0)

    def test_update_args_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(15, 1, -5)

    def test_update_args_invalid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(15, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(15, 1, 2, -6)

    def test_update_args_invalid_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(15, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(15, 1, 2, 3, -6)

class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=15)
        self.assertEqual("[Rectangle] (15) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=15)
        self.assertEqual("[Rectangle] (15) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=15)
        self.assertEqual("[Rectangle] (15) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=15, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (15) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=5, x=8, id=15, width=1, height=2)
        self.assertEqual("[Rectangle] (15) 8/5 - 1/2", str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        expected = "[Rectangle] (None) 10/10 - 10/10"
        self.assertEqual(expected, str(r))

    def test_update_kwargs_twice(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=15, x=1, height=2)
        r.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (15) 1/3 - 2/15", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="2")

    def test_update_kwargs_width_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="2")

    def test_update_kwargs_height_zero(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="2")

    def test_update_kwargs_x_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="2")

    def test_update_kwargs_y_negative(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(15, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (15) 10/6 - 2/4", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))


if __name__ == '__main__':
    unittest.main()
