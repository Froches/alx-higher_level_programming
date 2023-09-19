#!/usr/bin/python3
"""Rectangle testing class"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Tests a rectangle class"""

    def test_valid_constructor(self):
        rect = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 100)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(5, -10)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, -1)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, 1, -2)

if __name__ == '__main__':
    unittest.main()
