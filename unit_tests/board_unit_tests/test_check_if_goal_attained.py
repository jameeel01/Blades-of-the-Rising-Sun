"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from board import check_if_goal_attained

class Test(TestCase):
    def test_check_if_goal_attained_true(self):
        character = {"x-coordinate": 9, "y-coordinate": 9, "level": 3}
        actual = check_if_goal_attained(character, (9, 9))
        expected = True
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_at_goal_low_level(self):
        character = {"x-coordinate": 9, "y-coordinate": 9, "level": 2}
        actual = check_if_goal_attained(character, (9, 9))
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_not_at_goal_high_level(self):
        character = {"x-coordinate": 4, "y-coordinate": 9, "level": 5}
        actual = check_if_goal_attained(character, (9, 9))
        expected = False
        self.assertEqual(actual, expected)

    def test_check_if_goal_attained_not_at_goal_low_level(self):
        character = {"x-coordinate": 0, "y-coordinate": 0, "level": 1}
        actual = check_if_goal_attained(character, (9, 9))
        expected = False
        self.assertEqual(actual, expected)
