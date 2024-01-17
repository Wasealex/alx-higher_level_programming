#!/usr/bin/python3
"""tests for square methods
"""
from models.square import Square
from models.base import Base
import unittest
import sys
from io import StringIO


class TestSquareInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class
    """
    def test_one_args(self):
        s1 = Square(5)
        s2 = Square(10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(4, 6, 8)
        s2 = Square(3, 2, 1)
        self.assertEqual(s1.id, s2.id - 1)

    def test_one_args_print(self):
        s1 = Square(2)
        self.assertEqual(str(s1), "[Square] ({}) 0/0 - 2".format(s1.id))

    def test_three_args_print(self):
        s1 = Square(2, 2, 3)
        self.assertEqual(str(s1), "[Square] ({}) 2/3 - 2".format(s1.id))

    def test_four_args_print(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (4) 2/3 - 1")


    def test_five_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 1, 2)

class TestSquareErrors(unittest.TestCase):
    """testing different values for Square
    """
    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3", 4)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 3, -1, 0)


class TestSquareArea(unittest.TestCase):
    """testing area() method of class Square
    """
    def test_area_1(self):
        s1 = Square(2)
        self.assertEqual(4, s1.area())

    def test_area_2(self):
        s1 = Square(5, 10, 1, 5)
        self.assertEqual(25, s1.area())

class TestSquareDisplay(unittest.TestCase):
    """ unittest for testing the display() method of Square
    """
    @staticmethod
    def assert_printed(expected, test):
        output = StringIO()
        sys.stdout = output
        test()
        out = output.getvalue()
        sys.stdout = sys.__stdout__
        assert expected == out

    def test_display_size(self):
        s1 = Square(3, 0, 0)
        self.assert_printed("###\n###\n###\n", s1.display)

    def test_display_size_x(self):
        s = Square(3, 1, 0)
        self.assert_printed(" ###\n ###\n ###\n", s.display)

    def test_display_size_y(self):
        s = Square(4, 0, 1)
        o = "\n####\n####\n####\n####\n"
        self.assert_printed(o, s.display)

    def test_display_size_x_y(self):
        s = Square(2, 3, 2)
        o = "\n\n   ##\n   ##\n"
        self.assert_printed(o, s.display)

class TestSquare_to_dictionary(unittest.TestCase):
    """testing to_dictionary() method of the Square"""

    def test_to_dictionary_output(self):
        s = Square(1, 2, 3, 4)
        expected = {'size': 1, 'x': 2, 'y': 3, 'id': 4}
        self.assertDictEqual(expected, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 9)
        s2 = Square(5, 9, 1, 2)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

class TestSquare_update_args(unittest.TestCase):
    """testing update() method of the Square"""

    def test_update_args_zero(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        s = Square(10, 10, 10, 10)
        s.update(15)
        self.assertEqual("[Square] (15) 10/10 - 10", str(s))

    def test_update_args_two(self):
        s = Square(10, 10, 10, 10)
        s.update(15, 2)
        self.assertEqual("[Square] (15) 10/10 - 2", str(s))

    def test_update_args_three(self):
        s = Square(10, 10, 10, 10)
        s.update(15, 2, 3)
        self.assertEqual("[Square] (15) 3/10 - 2", str(s))

    def test_update_args_four(self):
        s = Square(10, 10, 10, 10)
        s.update(15, 2, 3, 4)
        self.assertEqual("[Square] (15) 3/4 - 2", str(s))

    def test_update_args_more_than_four(self):
        s = Square(10, 10, 10, 10)
        s.update(15, 2, 3, 4, 5, 6)
        self.assertEqual("[Square] (15) 3/4 - 2", str(s))

    def test_update_args_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(15, 2, 3, 4)
        s.update(6, 5, 4, 3)
        self.assertEqual("[Square] (6) 4/3 - 5", str(s))

    def test_update_args_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(15, "2")

    def test_update_args_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(15, 0)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(15, -5)

    def test_update_args_invalid_x_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(15, 2, "invalid")

    def test_update_args_x_negat(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(15, 1, -1)

    def test_update_args_x_negat(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(15, 1, -5)

    def test_update_args_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(15, 2, 3, "invalid")

    def test_update_args_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(15, 1, 2, -6)

class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Square class."""

    def test_update_kwargs_one(self):
        s = Square(10, 10, 10, 10)
        s.update(id=15)
        self.assertEqual("[Square] (15) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        s = Square(10, 10, 10, 10)
        s.update(size=2, id=15)
        self.assertEqual("[Square] (15) 10/10 - 2", str(s))

    def test_update_kwargs_three(self):
        s = Square(10, 10, 10, 10)
        s.update(id=15, x=1, size=4)
        self.assertEqual("[Square] (15) 1/10 - 4", str(s))

    def test_update_kwargs_four(self):
        s = Square(10, 10, 10, 10)
        s.update(y=5, x=8, id=15, size=1,)
        self.assertEqual("[Square] (15) 8/5 - 1", str(s))

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        expected = "[Square] (None) 10/10 - 10"
        self.assertEqual(expected, str(s))

    def test_update_kwargs_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(id=15, x=1, size=2)
        s.update(y=3, size=15, x=2)
        self.assertEqual("[Square] (15) 2/3 - 15", str(s))

    def test_update_kwargs_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="2")

    def test_update_kwargs_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-5)

    def test_update_kwargs_inavlid_x_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="2")

    def test_update_kwargs_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="2")

    def test_update_kwargs_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(15, 2, y=6)
        self.assertEqual("[Square] (15) 10/6 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

if __name__ == '__main__':
    unittest.main()
