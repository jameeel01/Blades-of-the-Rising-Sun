from unittest import TestCase
from unittest.mock import patch
from challenges import burning_village_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "1")
    def test_burning_village_samurai_save(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0
        }
        burning_village_challenge(character)

        actual = character
        expected = {
            "honor": 2,
            "experience": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "1")
    def test_burning_village_ronin_save(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        burning_village_challenge(character)

        actual = character
        expected = {
            "honor": 2,
            "experience": 1,
            "bond_with_Ryūichi": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "2")
    def test_burning_village_samurai_chase(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0
        }
        burning_village_challenge(character)

        actual = character
        expected = {
            "honor": 0,
            "experience": 2
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "2")
    def test_burning_village_ronin_chase(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        burning_village_challenge(character)

        actual = character
        expected = {
            "honor": 0,
            "experience": 2,
            "bond_with_Ryūichi": -1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "3")
    def test_burning_village_samurai_scavenge(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0
        }
        burning_village_challenge(character)

        actual = character
        expected = {
            "honor": -2,
            "experience": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "3")
    def test_burning_village_ronin_scavenge(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        burning_village_challenge(character)

        actual = character
        expected = {
            "honor": -2,
            "experience": 0,
            "bond_with_Ryūichi": -2
        }
        self.assertEqual(actual, expected)
