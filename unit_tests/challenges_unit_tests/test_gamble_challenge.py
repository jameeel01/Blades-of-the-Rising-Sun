"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import gamble_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly")
    @patch("challenges.random.randint", return_value = 8)
    def test_gamble_challenge_win(self, _, __):
        character = {
            "hp": 10,
            "max_hp": 10,
            "experience": 0
        }

        gamble_challenge(character)

        actual = character
        expected = {
            "hp": 10,
            "max_hp": 10,
            "experience": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("challenges.random.randint", return_value = 2)
    def test_gamble_challenge_lose_decrease_hp(self, _, __):
        character = {
            "hp": 10,
            "max_hp": 10,
            "experience": 0
        }

        gamble_challenge(character)

        actual = character
        expected = {
            "hp": 8,
            "max_hp": 10,
            "experience": 0
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("challenges.random.randint", return_value = 0)
    def test_gamble_challenge_lose_capped_0_hp(self, _, __):
        character = {
            "hp": 1,
            "max_hp": 10,
            "experience": 0
        }

        gamble_challenge(character)

        actual = character
        expected = {
            "hp": 0,
            "max_hp": 10,
            "experience": 0
        }
        self.assertEqual(actual, expected)