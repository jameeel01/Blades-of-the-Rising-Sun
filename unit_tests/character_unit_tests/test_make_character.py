"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from character import make_character

class Test(TestCase):
    def test_make_character_name(self):
        character = make_character("Jameel", "ronin")
        actual = character["name"]
        expected = "Jameel"
        self.assertEqual(actual, expected)

    def test_make_character_path(self):
        character = make_character("Aiko", "samurai")
        actual = character["path"]
        expected = "samurai"
        self.assertEqual(actual, expected)

    def test_make_character_hp(self):
        character = make_character("Test", "ronin")
        actual = character["hp"]
        expected = 20
        self.assertEqual(actual, expected)

    def test_make_character_max_hp(self):
        character = make_character("Test", "ronin")
        actual = character["max_hp"]
        expected = 20
        self.assertEqual(actual, expected)

    def test_make_character_attack_power(self):
        character = make_character("Test", "samurai")
        actual = character["attack_power"]
        expected = 3
        self.assertEqual(actual, expected)

    def test_make_character_level(self):
        character = make_character("Test", "ronin")
        actual = character["level"]
        expected = 1
        self.assertEqual(actual, expected)

    def test_make_character_experience(self):
        character = make_character("Test", "samurai")
        actual = character["experience"]
        expected = 0
        self.assertEqual(actual, expected)

    def test_make_character_coordinates(self):
        character = make_character("Test", "ronin")
        actual = (character["x-coordinate"], character["y-coordinate"])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_make_character_bond(self):
        character = make_character("Test", "samurai")
        actual = character["bond_with_Ryūichi"]
        expected = 0
        self.assertEqual(actual, expected)

    def test_make_character_honor(self):
        character = make_character("Test", "ronin")
        actual = character["honor"]
        expected = 0
        self.assertEqual(actual, expected)

    def test_make_character_betrayal(self):
        character = make_character("Test", "samurai")
        actual = character["betrayal"]
        expected = False
        self.assertEqual(actual, expected)

    def test_make_character_challenge_stack(self):
        character = make_character("Test", "ronin")
        actual = character["challenge_stack"]
        expected = None
        self.assertEqual(actual, expected)
