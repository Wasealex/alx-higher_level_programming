#!/usr/bin/python3
"""tests for base methods
"""
from models.base import Base
from models.rectangle import Rectangle
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

class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

if __name__ == '__main__':
    unittest.main()
