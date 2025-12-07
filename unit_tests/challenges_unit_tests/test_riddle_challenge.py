from unittest import TestCase
from unittest.mock import patch
from challenges import riddle_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly", return_value = None)
    @patch("builtins.input", return_value = "2")
    def test_riddle_challenge_samurai_correct_answer(self, _, __):
        character = {
            "hp": 10,
            "max_hp": 10,
            "experience": 0,
            "path": "samurai"
        }
        riddle_challenge(character)

        actual = character
        expected = {
            "hp": 10,
            "max_hp": 10,
            "experience": 1,
            "path": "samurai"
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("builtins.input", return_value = "1")
    def test_riddle_challenge_samurai_wrong_answer(self, _, __):
        character = {
            "hp": 10,
            "max_hp": 10,
            "experience": 0,
            "path": "samurai"
        }
        riddle_challenge(character)

        actual = character
        expected = {
            "hp": 8,
            "max_hp": 10,
            "experience": 0,
            "path": "samurai"
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("builtins.input", return_value = "2")
    def test_riddle_challenge_ronin_correct_answer(self, _, __):
        character = {
            "hp": 10,
            "max_hp": 10,
            "experience": 0,
            "bond_with_Ryūichi": 0,
            "path": "ronin"
        }
        riddle_challenge(character)

        actual = character
        expected = {
            "hp": 10,
            "max_hp": 10,
            "experience": 1,
            "bond_with_Ryūichi": 1,
            "path": "ronin"
        }
        self.assertEqual(actual, expected)

    @patch("challenges.type_text_slowly", return_value = None)
    @patch("builtins.input", return_value = "4")
    def test_riddle_challenge_ronin_wrong_answer(self, _, __):
        character = {
            "hp": 10,
            "max_hp": 10,
            "experience": 0,
            "bond_with_Ryūichi": 0,
            "path": "ronin"
        }
        riddle_challenge(character)

        actual = character
        expected = {
            "hp": 8,
            "max_hp": 10,
            "experience": 0,
            "bond_with_Ryūichi": 0,
            "path": "ronin"
        }
        self.assertEqual(actual, expected)