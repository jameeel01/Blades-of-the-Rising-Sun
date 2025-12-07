"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import pilgrim_challenge

class Test(TestCase):
    @patch("challenges.type_text_slowly")
    def test_pilgrim_challenge_experience_increases(self, _):
        character = {"experience": 5}
        pilgrim_challenge(character)

        actual = character
        expected = {"experience": 6}
        self.assertEqual(actual, expected)
