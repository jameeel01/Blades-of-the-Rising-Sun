from unittest import TestCase
from character import character_has_leveled

class Test(TestCase):
    def test_character_has_leveled_xp_to_2(self):
        actual = character_has_leveled({"level": 1, "experience": 5})
        expected = True
        self.assertEqual(actual, expected)

    def test_character_has_leveled_not_enough_xp_to_2(self):
        actual = character_has_leveled({"level": 1, "experience": 4})
        expected = False
        self.assertEqual(actual, expected)

    def test_character_has_leveled_xp_to_3(self):
        actual = character_has_leveled({"level": 2, "experience": 10})
        expected = True
        self.assertEqual(actual, expected)

    def test_character_has_leveled_not_enough_xp_to_3(self):
        actual = character_has_leveled({"level": 2, "experience": 9})
        expected = False
        self.assertEqual(actual, expected)

    def test_character_has_leveled_max(self):
        actual = character_has_leveled({"level": 3, "experience": 100})
        expected = False
        self.assertEqual(actual, expected)
