#!/usr/bin/python3
"""tests for base methods
"""
from models.base import Base
import unittest


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class
    """

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_base(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_id_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(3, 5)

if __name__ == '__main__':
    unittest.main()
