from unittest import TestCase
from challenges import ryuichi_present

class Test(TestCase):
    def test_ryuichi_present_returns_true_for_ronin(self):
        character = {"path": "ronin"}

        actual = True
        expected = ryuichi_present(character)
        self.assertEqual(actual, expected)

    def test_ryuichi_present_returns_false_for_samurai(self):
        character = {"path": "samurai"}

        actual = False
        expected = ryuichi_present(character)
        self.assertEqual(actual, expected)
