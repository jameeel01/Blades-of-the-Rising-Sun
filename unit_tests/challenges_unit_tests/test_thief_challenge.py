"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import thief_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly")
    def test_thief_challenge_decreases_experience(self, _):
        character = { "experience": 5}
        thief_challenge(character)

        actual = character
        expected = {"experience": 4}
        self.assertEqual(actual, expected)
