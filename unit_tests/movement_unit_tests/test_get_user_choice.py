"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from movement import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect = ['1'])
    def test_get_user_choice_valid_north(self, _):
        actual = get_user_choice()
        expected = 1
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect = ['', '2'])
    @patch('sys.stdout', new_callable = StringIO)
    def test_get_user_choice_blank_then_valid(self, _, __):
        actual = get_user_choice()
        expected = 2
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect = ['hello', '3'])
    @patch('sys.stdout', new_callable = StringIO)
    def test_get_user_choice_non_numeric_then_valid(self, _, __):
        actual = get_user_choice()
        expected = 3
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect = ['9', '4'])
    @patch('sys.stdout', new_callable = StringIO)
    def test_get_user_choice_out_of_range_then_valid(self, _, __):
        actual = get_user_choice()
        expected = 4
        self.assertEqual(actual, expected)
