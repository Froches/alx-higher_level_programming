#!/usr/bin/python3
"""Square testing class"""


import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_valid_constructor(self):
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_size_getter_setter(self):
        square = Square(3)

        self.assertEqual(square.size, 3)

        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_area(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)

    def test_str_method(self):
        square = Square(6, 2, 3, 42)
        self.assertEqual(str(square), "[Square] (42) 2/3 - 6")

    def test_update_method(self):
        square = Square(2, 1, 1, 1)

        square.update(5, 3, 3, 3)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 3)

        square.update(id=10, size=4, x=2, y=2)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 2)

if __name__ == '__main__':
    unittest.main()'
