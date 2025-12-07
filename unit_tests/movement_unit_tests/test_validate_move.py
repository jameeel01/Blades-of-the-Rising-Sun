"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from movement import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_north_valid(self):
        test_character = {"x-coordinate": 2, "y-coordinate": 2}
        actual = validate_move(test_character, 1)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_north_invalid_top_left(self):
        test_character = {"x-coordinate": 0, "y-coordinate": 0}
        actual = validate_move(test_character, 1)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_north_invalid_top_right(self):
        test_character = {"x-coordinate": 0, "y-coordinate": 9}
        actual = validate_move(test_character, 1)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_south_valid(self):
        test_character = {"x-coordinate": 2, "y-coordinate": 2}
        actual = validate_move(test_character, 2)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_south_invalid_bottom_right(self):
        test_character = {"x-coordinate": 9, "y-coordinate": 9}
        actual = validate_move(test_character, 2)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_south_invalid_bottom_left(self):
        test_character = {"x-coordinate": 9, "y-coordinate": 0}
        actual = validate_move(test_character, 2)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_east_valid(self):
        test_character = {"x-coordinate": 2, "y-coordinate": 2}
        actual = validate_move(test_character, 3)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_east_invalid_bottom_right(self):
        test_character = {"x-coordinate": 9, "y-coordinate": 9}
        actual = validate_move(test_character, 3)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_west_valid(self):
        test_character = {"x-coordinate": 2, "y-coordinate": 2}
        actual = validate_move(test_character, 4)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_west_invalid_bottom_left(self):
        test_character = {"x-coordinate": 9, "y-coordinate": 0}
        actual = validate_move(test_character, 4)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_invalid_direction(self):
        test_character = {"x-coordinate": 2, "y-coordinate": 2}
        actual = validate_move(test_character, 9)
        expected = False
        self.assertEqual(actual, expected)

