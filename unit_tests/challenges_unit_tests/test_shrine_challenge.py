from unittest import TestCase
from unittest.mock import patch
from challenges import shrine_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly")
    @patch("builtins.input", return_value = "1")
    def test_shrine_challenge_increase_hp(self, _, __):
        character = {
            "hp": 7,
            "max_hp": 10,
            "level": 1
        }
        shrine_challenge(character)

        actual = character
        expected = {
            "hp": 8,
            "max_hp": 10,
            "level": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("builtins.input", return_value = "1")
    def test_shrine_challenge_increase_capped_max_hp(self, _, __):
        character = {
            "hp": 9,
            "max_hp": 10,
            "level": 1
        }
        shrine_challenge(character)

        actual = character
        expected = {
            "hp": 10,
            "max_hp": 10,
            "level": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("builtins.input", return_value = "1")
    def test_shrine_challenge_increase_hp_level_3(self, _, __):
        character = {
            "hp": 2,
            "max_hp": 10,
            "level": 3
        }
        shrine_challenge(character)

        actual = character
        expected = {
            "hp": 5,
            "max_hp": 10,
            "level": 3
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("builtins.input", return_value = "2")
    def test_shrine_challenge_leave(self, _, __):
        character = {"hp": 5}
        shrine_challenge(character)

        actual = character
        expected = {"hp": 5}
        self.assertEqual(actual, expected)
