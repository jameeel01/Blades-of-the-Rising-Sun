from unittest import TestCase
from unittest.mock import patch
from challenges import hostage_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.random.randint", return_value = 7)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "1")
    def test_hostage_challenge_samurai_attack_success(self, _, __, ___, ____):
        character = {
            "honor": 0,
            "experience": 0}
        hostage_challenge(character)

        actual = character
        expected = {
            "honor": 1,
            "experience": 2}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.random.randint", return_value = 2)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "1")
    def test_hostage_challenge_samurai_attack_failure(self, _, __, ___, ____):
        character = {
            "honor": 0,
            "experience": 0}
        hostage_challenge(character)

        actual = character
        expected = {
            "honor": -1,
            "experience": 1}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.random.randint", return_value = 7)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "1")
    def test_hostage_challenge_ronin_attack_success(self, _, __, ___, ____):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0}
        hostage_challenge(character)

        actual = character
        expected = {
            "honor": 1,
            "experience": 2,
            "bond_with_Ryūichi": 1}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.random.randint", return_value = 2)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "1")
    def test_hostage_challenge_ronin_attack_failure(self, _, __, ___, ____):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        hostage_challenge(character)

        actual = character
        expected = {
            "honor": -1,
            "experience": 1,
            "bond_with_Ryūichi": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.random.randint", return_value = 2)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "2")
    def test_hostage_challenge_samurai_negotiate(self, _, __, ___, ____):
        character = {
            "honor": 0,
            "experience": 0}
        hostage_challenge(character)

        actual = character
        expected = {
            "honor": 1,
            "experience": 1}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.random.randint", return_value = 2)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "2")
    def test_hostage_challenge_ronin_negotiate(self, _, __, ___, ____):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        hostage_challenge(character)

        actual = character
        expected = {
            "honor": 1,
            "experience": 1,
            "bond_with_Ryūichi": 1
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.random.randint", return_value = 2)
    @patch("challenges.ryuichi_present", return_value = False)
    @patch("builtins.input", return_value = "3")
    def test_hostage_challenge_samurai_walk_away(self, _, __, ___, ____):
        character = {
            "honor": 0,
            "experience": 0}
        hostage_challenge(character)

        actual = character
        expected = {
            "honor": -2,
            "experience": 0}
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("challenges.random.randint", return_value = 2)
    @patch("challenges.ryuichi_present", return_value = True)
    @patch("builtins.input", return_value = "3")
    def test_hostage_challenge_ronin_walk_away(self, _, __, ___, ____):
        character = {
            "honor": 0,
            "experience": 0,
            "bond_with_Ryūichi": 0
        }
        hostage_challenge(character)

        actual = character
        expected = {
            "honor": -2,
            "experience": 0,
            "bond_with_Ryūichi": -1
        }
        self.assertEqual(actual, expected)