"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import training_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly")
    def test_training_challenge_increases_experience(self, _):
        character = {"experience": 4}
        training_challenge(character)

        actual = character
        expected = {"experience": 6}
        self.assertEqual(actual, expected)
