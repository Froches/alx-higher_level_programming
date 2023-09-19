#!/usr/bin/python3
"""Rectangle testing class"""

import unittest
from io import StringIO
import sys
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Tests a rectangle class"""

    def setUp(self):
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout

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

    def test_display(self):
        rect = Rectangle(3, 2)
        expected_output = "###\n###\n"

        rect.display()
        actual_output = sys.stdout.getvalue()

        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
