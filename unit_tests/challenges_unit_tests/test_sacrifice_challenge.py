"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import sacrifice_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "1")
    def test_sacrifice_challenge_samurai_offer_blood(self, _, __, ___):
        character = {
            "hp": 10,
            "max_hp": 20,
            "honor": 0,
            "attack_power": 3,
            "experience": 0
        }
        sacrifice_challenge(character)

        actual = character
        expected = {
            "hp": 8,
            "max_hp": 20,
            "honor": -2,
            "attack_power": 5,
            "experience": 2
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "1")
    def test_sacrifice_challenge_ronin_offer_blood(self, _, __, ___):
        character = {
            "hp": 10,
            "max_hp": 20,
            "honor": 0,
            "attack_power": 3,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        sacrifice_challenge(character)

        actual = character
        expected = {
            "hp": 8,
            "max_hp": 20,
            "honor": -2,
            "attack_power": 5,
            "experience": 2,
            "bond_with_Ryūichi": -1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "2")
    def test_sacrifice_challenge_samurai_refuse(self, _, __, ___):
        character = {
            "hp": 10,
            "max_hp": 20,
            "honor": 0,
            "attack_power": 3,
            "experience": 0
        }
        sacrifice_challenge(character)

        actual = character
        expected = {
            "hp": 10,
            "max_hp": 20,
            "honor": 2,
            "attack_power": 3,
            "experience": 0
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "2")
    def test_sacrifice_challenge_ronin_refuse(self, _, __, ___):
        character = {
            "hp": 10,
            "max_hp": 20,
            "honor": 0,
            "attack_power": 3,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        sacrifice_challenge(character)

        actual = character
        expected = {
            "hp": 10,
            "max_hp": 20,
            "honor": 2,
            "attack_power": 3,
            "experience": 0,
            "bond_with_Ryūichi": 1
        }
        self.assertEqual(actual, expected)