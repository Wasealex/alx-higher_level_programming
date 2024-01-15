#!/usr/bin/python3
"""tests for base methods
"""
from models.base import Base
from models.square import Square
import unittest


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class
    """

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(20)
        self.assertEqual(s1.id, s2.id - 1)

if __name__ == '__main__':
    unittest.main()
