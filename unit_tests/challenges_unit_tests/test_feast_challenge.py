from unittest import TestCase
from unittest.mock import patch
from challenges import feast_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly")
    def test_feast_challenge_increases_hp(self, _):
        character = {"hp": 5, "max_hp": 10}
        feast_challenge(character)

        actual = character
        expected = {"hp": 8, "max_hp": 10}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    def test_feast_challenge_capped_max_hp(self, _):
        character = {"hp": 9, "max_hp": 10}
        feast_challenge(character)

        actual = character
        expected = {"hp": 10, "max_hp": 10}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    def test_feast_challenge_max_hp(self, _):
        character = {"hp": 10, "max_hp": 10}
        feast_challenge(character)

        actual = character
        expected = {"hp": 10, "max_hp": 10}
        self.assertEqual(actual, expected)