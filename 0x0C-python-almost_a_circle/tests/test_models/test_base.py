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

if __name__ == '__main__':
    unittest.main()
