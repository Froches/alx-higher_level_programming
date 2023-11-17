#!/usr/bin/python3
"""Rectangle testing class"""

import unittest
from io import StringIO
import sys
from models.base import Base
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

    def test_display_with_x_y(self):
        rect = Rectangle(3, 2, 2, 3, 100)
        expected_output = "\n\n\n  ###\n  ###\n"

        rect.display()
        actual_output = sys.stdout.getvalue()

        self.assertEqual(actual_output, expected_output)

    def test_str_method(self):
        rect = Rectangle(3, 2, 1, 1, 100)
        expected_output = "[Rectangle] (100) 1/1 - 3/2"

        actual_output = str(rect)

        self.assertEqual(actual_output, expected_output)

    def test_update_with_args(self):
        rect = Rectangle(3, 2, 1, 1, 100)

        rect.update(200, 5, 6, 2, 3)

        self.assertEqual(rect.id, 200)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_update_with_kwargs(self):
        rect = Rectangle(3, 2, 1, 1, 100)

        rect.update(id=200, width=5, height=6, x=2, y=3)

        self.assertEqual(rect.id, 200)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 6)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_to_dictionary(self):
        rect = Rectangle(5, 10, 2, 3, 42)
        rect_dict = rect.to_dictionary()

        self.assertEqual(rect_dict, {
            'id': 42,
            'width': 5,
            'height': 10,
            'x': 2,
            'y': 3
            })


if __name__ == '__main__':
    unittest.main()
