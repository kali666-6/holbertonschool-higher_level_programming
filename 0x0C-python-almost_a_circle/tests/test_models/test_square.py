#!/usr/bin/python3

'''
Unittest for square
'''

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import json
import unittest

class TestSquareMethods(unittest.TestCase):
    def test_square(self):
        '''Basics tests for Square objects creation'''
        s1 = Square(1)
        self.assertEqual(s1.id, 30)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(1, 2)
        self.assertEqual(s2.id, 31)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 0)

        s3 = Square(1, 2, 3)
        self.assertEqual(s3.id, 32)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)

        s4 = Square(1, 2, 3, 150)
        self.assertEqual(s4.id, 150)
        self.assertEqual(s4.size, 1)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 3)

        error_msg = 'width must be an integer'
        with self.assertRaises(TypeError)as error:
            s4 = Rectangle("1", 2)
        self.assertEqual(error_msg, str(error.exception))

if __name__ == '__main__':
    unittest.main()
