"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import ambush_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly")
    @patch("challenges.random.randint", return_value = 3)
    def test_ambush_challenge_decreases_hp(self, _, __):
        character = {"hp": 10, "max_hp": 20}
        ambush_challenge(character)

        actual = character
        expected = {"hp": 7, "max_hp": 20}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("challenges.random.randint", return_value = 4)
    def test_ambush_challenge_capped_0_hp(self, _, __):
        character = {"hp": 1, "max_hp": 20}
        ambush_challenge(character)

        actual = character
        expected = {"hp": 0, "max_hp": 20}
        self.assertEqual(actual, expected)