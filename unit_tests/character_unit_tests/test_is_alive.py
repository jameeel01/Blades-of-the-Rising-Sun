"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from character import is_alive

class Test(TestCase):
    def test_is_alive_positive_hp(self):
        actual = is_alive({"hp": 7})
        expected = True
        self.assertEqual(actual, expected)

    def test_is_alive_zero_hp(self):
        actual = is_alive({"hp": 0})
        expected = False
        self.assertEqual(actual, expected)

    def test_is_alive_negative_hp(self):
        actual = is_alive({"hp": -3})
        expected = False
        self.assertEqual(actual, expected)