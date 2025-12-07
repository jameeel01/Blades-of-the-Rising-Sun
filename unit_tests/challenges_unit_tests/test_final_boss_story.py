"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from unittest.mock import patch
from challenges import final_boss_story

class Test(TestCase):
    @patch("challenges.final_boss_outro_samurai")
    @patch("challenges.print_final_duel_banner")
    @patch("challenges.final_boss_intro_samurai")
    @patch("challenges.boss_fight", return_value = True)
    def test_final_boss_story_victory(self, _, __, ___, ____):
        character = {
            "path": "samurai",
            "friend_name": "Ryūichi",
            "bond_with_Ryūichi": 0,
            "betrayal": False
        }

        actual = final_boss_story(character)
        expected = True
        self.assertEqual(actual, expected)

    @patch("challenges.betrayal_spared_scene")
    @patch("challenges.betrayal_confrontation_intro")
    @patch("challenges.emperor_death_scene")
    @patch("challenges.print_final_duel_banner")
    @patch("challenges.final_boss_intro_ronin")
    @patch("challenges.boss_fight", return_value = True)
    def test_final_boss_story_ronin_betrayal_spared(self, _, __, ___, ____, _____, ______):
        character = {
            "path": "ronin",
            "bond_with_Ryūichi": 5,
            "betrayal": True
        }

        actual = final_boss_story(character)
        expected = True
        self.assertEqual(actual, expected)

    @patch("challenges.betrayal_duel_scene")
    @patch("challenges.betrayal_confrontation_intro")
    @patch("challenges.emperor_death_scene")
    @patch("challenges.print_final_duel_banner")
    @patch("challenges.final_boss_intro_ronin")
    @patch("challenges.boss_fight", return_value = True)
    def test_final_boss_story_ronin_betrayal_duel(self, _, __, ___, ____, _____, ______):
        character = {
            "path": "ronin",
            "bond_with_Ryūichi": 0,
            "betrayal": True
        }

        actual = final_boss_story(character)
        expected = True
        self.assertEqual(actual, expected)

    @patch("challenges.rebuild_scene")
    @patch("challenges.emperor_death_scene")
    @patch("challenges.print_final_duel_banner")
    @patch("challenges.final_boss_intro_ronin")
    @patch("challenges.boss_fight", return_value = True)
    def test_final_boss_story_ronin_rebuild(self, _, __, ___, ____, _____):
        character = {
            "path": "ronin",
            "bond_with_Ryūichi": 5,
            "betrayal": False
        }

        actual = final_boss_story(character)
        expected = True
        self.assertEqual(actual, expected)

    @patch("challenges.abandonment_scene")
    @patch("challenges.emperor_death_scene")
    @patch("challenges.print_final_duel_banner")
    @patch("challenges.final_boss_intro_ronin")
    @patch("challenges.boss_fight", return_value = True)
    def test_final_boss_story_ronin_abandonment(self, _, __, ___, ____, _____):
        character = {
            "path": "ronin",
            "bond_with_Ryūichi": 0,
            "betrayal": False
        }

        actual = final_boss_story(character)
        expected = True
        self.assertEqual(actual, expected)

    @patch("challenges.print_final_duel_banner")
    @patch("challenges.final_boss_intro_ronin")
    @patch("challenges.boss_fight", return_value = False)
    def test_final_boss_story_ronin_emperor_kills_player(self, _, __, ___):
        character = {
            "path": "ronin",
            "bond_with_Ryūichi": 5,
            "betrayal": False
        }

        actual = final_boss_story(character)
        expected = False
        self.assertEqual(actual, expected)
