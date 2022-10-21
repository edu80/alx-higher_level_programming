#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test_maxinteger class to test the max_integer function"""

    def test_normals(self):
        """Normal cases"""
        self.assertEqual(max_integer([3, 4, 5]), 5)
        self.assertEqual(max_integer([-6, -2, 5]), 5)
        self.assertEqual(max_integer([-4, -32, -3]), -3)
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_list_is_empty(self):
        """An empty list is given as parameter"""
        self.assertEqual(max_integer([]), None)

    def test_max_int_list(self):
        """"Find the max in a list of ints"""
        list_1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list_1), max(list_1))

    def test_max_float_list(self):
        """Find the max in a list of floats"""
        list_2 = [2.3, 7.3, 2.6, 3.3, 5.9]
        self.assertEqual(max_integer(list_2), max(list_2))

    def test_max_float_int_list(self):
        """Find the max in a list of int and floats"""
        list_3 = [2.3, 7.3, 2.6, 3.3, 5.9, 4, 8, 11, 12]
        self.assertEqual(max_integer(list_3), max(list_3))

    def test_negative_list(self):
        """Find the max in a list of negative int and floats"""
        list_4 = [-2.3, -7.3, -2.6, -3.3, -5.9, -4, -8, -11, -12]
        self.assertEqual(max_integer(list_4), max(list_4))

    def test_argument_is_string(self):
        """Raise TypeError if the argument is a string"""
        with self.assertRaises(TypeError):
            max_integer("Hello world", 1)

    def test_argument_is_tuple(self):
        """Raise TypeError if the argument is a tuple"""
        with self.assertRaises(TypeError):
            max_integer(1, 2, 3)

    def test_argument_is_int_float(self):
        """Raise TypeError if the argument is a int or float"""
        with self.assertRaises(TypeError):
            max_integer(3)
        with self.assertRaises(TypeError):
            max_integer(3.4)

    def test_argument_is_boolean(self):
        """Raise TypeError if the argument is a bool"""
        with self.assertRaises(TypeError):
            max_integer(True)

    def test_special_chars(self):
        """
        Test error cases
        """
        with self.assertRaises(TypeError):
            max_integer("", "")

if __name__ == '__main__':
    unittest.main()
