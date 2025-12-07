from unittest import TestCase
from unittest.mock import patch
from challenges import bridge_challenge

class Test(TestCase):

    @patch("challenges.type_text_slowly")
    @patch("challenges.type_text_slowly")
    @patch("challenges.random.randint", return_value = 6)
    def test_bridge_challenge_safe(self, _, __, ___):
        character = {"hp": 10, "max_hp": 20}
        bridge_challenge(character)

        actual = character
        expected = {"hp": 10, "max_hp": 20}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("challenges.type_text_slowly")
    @patch("challenges.random.randint", return_value = 2)
    def test_bridge_challenge_fall(self, _, __, ___):
        character = {"hp": 10, "max_hp": 20}
        bridge_challenge(character)

        actual = character
        expected = {"hp": 8, "max_hp": 20}
        self.assertEqual(actual, expected)