from unittest import TestCase
from unittest.mock import patch
from challenges import execution_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "1")
    def test_execution_challenge_samurai_intervene(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0
        }

        execution_challenge(character)

        actual = character
        expected = {
            "honor": -1,
            "experience": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "1")
    def test_execution_challenge_ronin_intervene(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }

        execution_challenge(character)

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
    def test_execution_challenge_samurai_observe(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0
        }

        execution_challenge(character)

        actual = character
        expected = {
            "honor": -2,
            "experience": 0
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "2")
    def test_execution_challenge_ronin_observe(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }

        execution_challenge(character)

        actual = character
        expected = {
            "honor": -2,
            "experience": 0,
            "bond_with_Ryūichi": -1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "3")
    def test_execution_challenge_samurai_aid_executioner(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0
        }

        execution_challenge(character)

        actual = character
        expected = {
            "honor": -3,
            "experience": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "3")
    def test_execution_challenge_ronin_aid_executioner(self, _, __, ___):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }

        execution_challenge(character)

        actual = character
        expected = {
            "honor": -3,
            "experience": 1,
            "bond_with_Ryūichi": -2
        }
        self.assertEqual(actual, expected)