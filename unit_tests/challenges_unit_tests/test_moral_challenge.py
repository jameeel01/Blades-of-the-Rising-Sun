"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import moral_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly")
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "1")
    def test_moral_challenge_samurai_kill_thief(self, _, __, ___):
        character = {
            "experience": 0,
            "honor": 0,
            "bond_with_Ryūichi": 0,
            "name": "Test"
        }
        moral_challenge(character)

        actual = character
        expected = {
            "experience": 1,
            "honor": -2,
            "bond_with_Ryūichi": 0,
            "name": "Test"
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "2")
    def test_moral_challenge_samurai_spare_thief(self, _, __, ___):
        character = {
            "experience": 0,
            "honor": 0,
            "bond_with_Ryūichi": 0,
            "name": "Test"
        }
        moral_challenge(character)

        actual = character
        expected = {
            "experience": 0,
            "honor": 0,
            "bond_with_Ryūichi": 0,
            "name": "Test"
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "3")
    def test_moral_challenge_samurai_give_food(self, _, __, ___):
        character = {
            "experience": 0,
            "honor": 0,
            "bond_with_Ryūichi": 0,
            "name": "Test"
        }
        moral_challenge(character)

        actual = character
        expected = {
            "experience": 0,
            "honor": 2,
            "bond_with_Ryūichi": 0,
            "name": "Test"
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "1")
    def test_moral_challenge_ronin_kill_thief(self, _, __, ___):
        character = {
            "experience": 0,
            "honor": 0,
            "bond_with_Ryūichi": 0,
            "name": "Test"
        }
        moral_challenge(character)

        actual = character
        expected = {
            "experience": 1,
            "honor": -2,
            "bond_with_Ryūichi": -1,
            "name": "Test"
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "2")
    def test_moral_challenge_ronin_spare_thief(self, _, __, ___):
        character = {
            "experience": 0,
            "honor": 0,
            "bond_with_Ryūichi": 0,
            "name": "Test"
        }
        moral_challenge(character)

        actual = character
        expected = {
            "experience": 0,
            "honor": 0,
            "bond_with_Ryūichi": 1,
            "name": "Test"
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "3")
    def test_moral_challenge_ronin_give_food(self, _, __, ___):
        character = {
            "experience": 0,
            "honor": 0,
            "bond_with_Ryūichi": 0,
            "name": "Test"
        }
        moral_challenge(character)

        actual = character
        expected = {
            "experience": 0,
            "honor": 2,
            "bond_with_Ryūichi": 2,
            "name": "Test"
        }
        self.assertEqual(actual, expected)


