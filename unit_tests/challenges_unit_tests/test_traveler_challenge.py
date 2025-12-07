"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import traveler_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly")
    @patch("builtins.input", return_value = "1")
    def test_traveler_challenge_ronin_help(self, _, __):
        character = {
            "path": "ronin",
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        traveler_challenge(character)

        actual = character
        expected = {
            "path": "ronin",
            "honor": 1,
            "experience": 1,
            "bond_with_Ryūichi": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("builtins.input", return_value = "2")
    def test_traveler_challenge_ronin_ignore(self, _, __):
        character = {
            "path": "ronin",
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        traveler_challenge(character)

        actual = character
        expected = {
            "path": "ronin",
            "honor": -1,
            "experience": 0,
            "bond_with_Ryūichi": -1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("builtins.input", return_value = "1")
    def test_traveler_challenge_samurai_help(self, _, __):
        character = {
            "path": "samurai",
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        traveler_challenge(character)

        actual = character
        expected = {
            "path": "ronin",
            "honor": 1,
            "experience": 1,
            "bond_with_Ryūichi": 0
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly")
    @patch("builtins.input", return_value = "2")
    def test_traveler_challenge_samurai_help(self, _, __):
        character = {
            "path": "samurai",
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        traveler_challenge(character)

        actual = character
        expected = {
            "path": "samurai",
            "honor": -1,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        self.assertEqual(actual, expected)