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

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_id_str(self):
        self.assertEqual("ALX", Base("ALX").id)

    def test_id_float(self):
        self.assertEqual(12.5, Base(12.5).id)

    def test_id_complex(self):
        self.assertEqual(complex(15), Base(complex(15)).id)

    def test_id_dictionary(self):
        self.assertEqual({"Alpha": 1, "B": 2}, Base({"Alpha": 1, "B": 2}).id)

    def test_id_bool(self):
        self.assertEqual(True, Base(True).id)

    def test_id_list(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

if __name__ == '__main__':
    unittest.main()
