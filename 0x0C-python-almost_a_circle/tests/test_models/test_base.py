#!/usr/bin/python3
"""Unit tests for base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for the base class"""

    def test_assignment_with_args(self):
        """Tests id assignment with arguments"""

        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_assignment_with_no_args(self):
        """Tests id assignment without arguments"""

        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_auto_id_assignment(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()

        assert obj1.id != obj2.id
        assert obj2.id != obj3.id
        assert obj3.id != obj1.id


if __name__ == '__main__':
    unittest.main()
