"""
Jameel Mohammed
A01430376
"""
from unittest import TestCase
from board import make_board

class Test(TestCase):
    def test_make_board_valid_10x10(self):
        board = make_board(10, 10)
        actual = len(board)
        expected = 100
        self.assertEqual(actual, expected)

    def test_make_board_valid_1x1(self):
        board = make_board(1, 1)
        actual = len(board)
        expected = 1
        self.assertEqual(actual, expected)

    def test_make_board_valid_rectangular(self):
        board = make_board(3, 7)
        actual = len(board)
        expected = 21
        self.assertEqual(actual, expected)

    def test_make_board_zero_rows(self):
        board = make_board(0, 5)
        actual = len(board)
        expected = 0
        self.assertEqual(actual, expected)

    def test_make_board_zero_columns(self):
        board = make_board(5, 0)
        actual = len(board)
        expected = 0
        self.assertEqual(actual, expected)

    def test_make_board_negative(self):
        board = make_board(-2, -2)
        actual = len(board)
        expected = 0
        self.assertEqual(actual, expected)
