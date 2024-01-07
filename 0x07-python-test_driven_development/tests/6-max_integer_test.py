#!/usr/bin/python3
"""Unittests for max_integer([..])
"""
import unittest
maxx = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])"""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [11, 12, 13, 14]
        self.assertEqual(maxx(ordered), 14)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [21, 22, 24, 23]
        self.assertEqual(maxx(unordered), 24)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [34, 33, 32, 31]
        self.assertEqual(maxx(max_at_beginning), 34)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(maxx(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [107]
        self.assertEqual(maxx(one_element), 107)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0, 0]
        self.assertEqual(maxx(floats), 15.2)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(maxx(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(maxx(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(maxx(""), None)

if __name__ == '__main__':
    unittest.main()
