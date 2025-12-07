from unittest import TestCase
from board import make_board, describe_current_location
from unittest.mock import patch
from io import StringIO

class Test(TestCase):
    @patch("sys.stdout", new_callable = StringIO)
    def test_describe_current_location_center(self, _):
        board = make_board(10, 10)
        character = {
            "x-coordinate": 4,
            "y-coordinate": 6,
            "hp": 10,
            "max_hp": 20,
            "level": 2,
            "experience": 3
        }
        describe_current_location(board, character)

        actual = _.getvalue()
        expected = (
            "\nLocation: (4, 6)\n"
            f"{board[(4, 6)]}\n"
            "HP: 10/20 | Level: 2 | XP: 3\n"
        )
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable = StringIO)
    def test_describe_current_location_top_left(self, _):
        board = make_board(10, 10)
        character = {
            "x-coordinate": 0,
            "y-coordinate": 0,
            "hp": 5,
            "max_hp": 20,
            "level": 1,
            "experience": 0
        }
        describe_current_location(board, character)

        actual = _.getvalue()
        expected = (
            "\nLocation: (0, 0)\n"
            f"{board[(0, 0)]}\n"
            "HP: 5/20 | Level: 1 | XP: 0\n"
        )
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable = StringIO)
    def test_describe_current_location_bottom_right(self, _):
        board = make_board(10, 10)
        character = {
            "x-coordinate": 9,
            "y-coordinate": 9,
            "hp": 20,
            "max_hp": 20,
            "level": 3,
            "experience": 10
        }
        describe_current_location(board, character)

        actual = _.getvalue()
        expected = (
            "\nLocation: (9, 9)\n"
            f"{board[(9, 9)]}\n"
            "HP: 20/20 | Level: 3 | XP: 10\n"
        )
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable = StringIO)
    def test_describe_current_location_low_hp(self, _):
        board = make_board(10, 10)
        character = {
            "x-coordinate": 3,
            "y-coordinate": 7,
            "hp": 1,
            "max_hp": 20,
            "level": 2,
            "experience": 6
        }
        describe_current_location(board, character)

        actual = _.getvalue()
        expected = (
            "\nLocation: (3, 7)\n"
            f"{board[(3, 7)]}\n"
            "HP: 1/20 | Level: 2 | XP: 6\n"
        )
        self.assertEqual(actual, expected)

    @patch("sys.stdout", new_callable=StringIO)
    def test_describe_current_location_high_xp_low_level(self, _):
        board = make_board(10, 10)
        character = {
            "x-coordinate": 8,
            "y-coordinate": 2,
            "hp": 12,
            "max_hp": 20,
            "level": 1,
            "experience": 9
        }
        describe_current_location(board, character)

        actual = _.getvalue()
        expected = (
            "\nLocation: (8, 2)\n"
            f"{board[(8, 2)]}\n"
            "HP: 12/20 | Level: 1 | XP: 9\n"
        )
        self.assertEqual(actual, expected)