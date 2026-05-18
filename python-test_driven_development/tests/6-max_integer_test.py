#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        self.assertIsNone(max_integer())

    def test_all_same(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-10, 0, 5, -3]), 5)

    def test_single_negative(self):
        self.assertEqual(max_integer([-7]), -7)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 2, 3.7]), 3.7)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)

    def test_duplicates(self):
        self.assertEqual(max_integer([3, 1, 3, 2]), 3)


if __name__ == '__main__':
    unittest.main()
