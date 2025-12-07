"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from character import execute_level_up

class Test(TestCase):
    @patch("pyfiglet.figlet_format")
    @patch("user_interface.type_text_slowly")
    def test_execute_level_up_1_to_2(self, _, __):
        character = {
            "level": 1,
            "max_hp": 20,
            "hp": 10,
            "attack_power": 3,
            "path": "ronin"
        }
        execute_level_up(character)

        actual = (
            character["level"],
            character["max_hp"],
            character["attack_power"],
            character["hp"]
        )
        expected = (2, 25, 6, 25)
        self.assertEqual(actual, expected)

    @patch("pyfiglet.figlet_format")
    @patch("user_interface.type_text_slowly")
    def test_execute_level_up_2_to_3(self, _, __):
        character = {
            "level": 2,
            "max_hp": 25,
            "hp": 10,
            "attack_power": 6,
            "path": "samurai"
        }
        execute_level_up(character)

        actual = (
            character["level"],
            character["max_hp"],
            character["attack_power"],
            character["hp"]
        )
        expected = (3, 30, 9, 30)
        self.assertEqual(actual, expected)

    @patch("pyfiglet.figlet_format")
    @patch("user_interface.type_text_slowly")
    def test_execute_level_up_max_is_3(self, _, __):
        character = {
            "level": 3,
            "max_hp": 30,
            "hp": 10,
            "attack_power": 9,
            "path": "ronin"
        }

        execute_level_up(character)
        actual = (
            character["level"],
            character["max_hp"],
            character["attack_power"],
            character["hp"]
        )
        expected = (3, 30, 9, 10)
        self.assertEqual(actual, expected)