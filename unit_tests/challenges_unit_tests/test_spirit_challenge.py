"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import spirit_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly")
    def test_spirit_challenge_increases_experience(self, _):
        character = {
            "honor": 3,
            "hp": 10,
            "experience": 2
        }
        spirit_challenge(character)

        actual = character
        expected = {
            "honor": 3,
            "hp": 10,
            "experience": 4
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    def test_spirit_challenge_decreases_hp(self, _):
        character = {
            "honor": -3,
            "hp": 10,
            "experience": 2
        }
        spirit_challenge(character)

        actual = character
        expected = {
            "honor": -3,
            "hp": 8,
            "experience": 2
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    def test_spirit_challenge_capped_0_hp(self, _):
        character = {
            "honor": -3,
            "hp": 1,
            "experience": 2
        }
        spirit_challenge(character)

        actual = character
        expected = {
            "honor": -3,
            "hp": 0,
            "experience": 2
        }
        self.assertEqual(actual, expected)