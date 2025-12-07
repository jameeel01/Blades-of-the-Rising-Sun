from unittest import TestCase
from unittest.mock import patch
from challenges import duel_of_honor_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "1")
    def test_duel_of_honor_samurai_accept(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0
        }
        duel_of_honor_challenge(character)

        actual = character
        expected = {
            "honor": 2,
            "experience": 2
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "1")
    def test_duel_of_honor_ronin_accept(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        duel_of_honor_challenge(character)

        actual = character
        expected = {
            "honor": 2,
            "experience": 2,
            "bond_with_Ryūichi": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "2")
    def test_duel_of_honor_samurai_fight_dirty(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0
        }
        duel_of_honor_challenge(character)

        actual = character
        expected = {
            "honor": -2,
            "experience": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "2")
    def test_duel_of_honor_ronin_fight_dirty(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        duel_of_honor_challenge(character)

        actual = character
        expected = {
            "honor": -2,
            "experience": 1,
            "bond_with_Ryūichi": -1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "3")
    def test_duel_of_honor_samurai_refuse(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0
        }
        duel_of_honor_challenge(character)

        actual = character
        expected = {
            "honor": -1,
            "experience": 0
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "3")
    def test_duel_of_honor_ronin_refuse(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        duel_of_honor_challenge(character)

        actual = character
        expected = {
            "honor": -1,
            "experience": 0,
            "bond_with_Ryūichi": -1
        }
        self.assertEqual(actual, expected)