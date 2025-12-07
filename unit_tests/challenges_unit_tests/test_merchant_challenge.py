"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import merchant_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly")
    def test_merchant_challenge_increase_hp(self, _):
        character = {"hp": 5, "max_hp": 10}
        merchant_challenge(character)

        actual = character
        expected = {"hp": 7, "max_hp": 10}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    def test_merchant_challenge_capped_max_hp(self, _):
        character = {"hp": 9, "max_hp": 10}
        merchant_challenge(character)

        actual = character
        expected = {"hp": 10, "max_hp": 10}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    def test_merchant_challenge_max_hp(self, _):
        character = {"hp": 10, "max_hp": 10}
        merchant_challenge(character)

        actual = character
        expected = {"hp": 10, "max_hp": 10}
        self.assertEqual(actual, expected)
