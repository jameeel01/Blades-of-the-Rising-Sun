"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from movement import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        test_character = {"x-coordinate": 2, "y-coordinate": 2}
        move_character(test_character, 1)
        actual = test_character
        expected = {"x-coordinate": 1, "y-coordinate": 2}
        self.assertEqual(actual, expected)

    def test_move_character_south(self):
        test_character = {"x-coordinate": 2, "y-coordinate": 2}
        move_character(test_character, 2)
        actual = test_character
        expected = {"x-coordinate": 3, "y-coordinate": 2}
        self.assertEqual(actual, expected)

    def test_move_character_east(self):
        test_character = {"x-coordinate": 2, "y-coordinate": 2}
        move_character(test_character, 3)
        actual = test_character
        expected = {"x-coordinate": 2, "y-coordinate": 3}
        self.assertEqual(actual, expected)

    def test_move_character_west(self):
        test_character = {"x-coordinate": 2, "y-coordinate": 2}
        move_character(test_character, 4)
        actual = test_character
        expected = {"x-coordinate": 2, "y-coordinate": 1}
        self.assertEqual(actual, expected)

    def test_move_character_invalid_direction_does_nothing(self):
        test_character = {"x-coordinate": 2, "y-coordinate": 2}
        move_character(test_character, 9)
        actual = test_character
        expected = {"x-coordinate": 2, "y-coordinate": 2}
        self.assertEqual(actual, expected)
