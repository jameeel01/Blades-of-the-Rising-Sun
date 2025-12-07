"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import wounded_soldier_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "1")
    def test_wounded_soldier_challenge_samurai_heal_soldier(self, _, __, ___):
        character = {"honor": 0}
        wounded_soldier_challenge(character)

        actual = character
        expected = {"honor": 1}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "1")
    def test_wounded_soldier_challenge_ronin_heal_soldier(self, _, __, ___):
        character = {"honor": 0, "bond_with_Ryūichi": 0}
        wounded_soldier_challenge(character)

        actual = character
        expected = {"honor": 1, "bond_with_Ryūichi": 2}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "2")
    def test_wounded_soldier_challenge_samurai_kill_soldier(self, _, __, ___):
        character = {"honor": 0}
        wounded_soldier_challenge(character)

        actual = character
        expected = {"honor": -1}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "2")
    def test_wounded_soldier_challenge_ronin_kill_soldier(self, _, __, ___):
        character = {"honor": 0, "bond_with_Ryūichi": 0}
        wounded_soldier_challenge(character)

        actual = character
        expected = {"honor": -1, "bond_with_Ryūichi": -1}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "3")
    def test_wounded_soldier_challenge_samurai_leave_soldier(self, _, __, ___):
        character = {"honor": 0}
        wounded_soldier_challenge(character)

        actual = character
        expected = {"honor": -2}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "3")
    def test_wounded_soldier_challenge_ronin_leave_soldier(self, _, __, ___):
        character = {"honor": 0, "bond_with_Ryūichi": 0}
        wounded_soldier_challenge(character)

        actual = character
        expected = {"honor": -2, "bond_with_Ryūichi": -2}
        self.assertEqual(actual, expected)
