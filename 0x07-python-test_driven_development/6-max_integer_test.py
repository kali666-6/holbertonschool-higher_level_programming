#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([4, 2, 3]), 4)
        self.assertEqual(max_integer([1, 5, 3]), 5)
        self.assertEqual(max_integer([-1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([2]), 2)
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))
