"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import assassin_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.random.randint", return_value = 4)
    def test_assassin_challenge_decrease_hp(self, _, __):
        character = {
            "hp": 10,
            "max_hp": 20
        }
        assassin_challenge(character)

        actual = character
        expected = {
            "hp": 6,
            "max_hp": 20
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.random.randint", return_value = 3)
    def test_assassin_challenge_capped_hp_at_0(self, _, __):
        character = {
            "hp": 1,
            "max_hp": 20
        }
        assassin_challenge(character)

        actual = character
        expected = {
            "hp": 0,
            "max_hp": 20
        }
        self.assertEqual(actual, expected)