"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import blessing_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly")
    @patch("challenges.type_text_slowly")
    def test_blessing_challenge_increases_experience(self, _, __):
        character = {"experience": 3}
        blessing_challenge(character)

        actual = character
        expected = {"experience": 4}
        self.assertEqual(actual, expected)