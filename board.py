"""
Jameel Mohammed
A01430376
"""
import random

def make_board(rows, columns):
    """
    Create a dictionary-based 10x10 game board filled with random room descriptions.

    :param rows: an integer representing how many rows the board has
    :param columns: an integer representing how many columns the board has
    :precondition: rows and columns must be positive integers greater than zero
    :postcondition: creates a dictionary where each tuple (row, column) has a random room description
    :return: a dictionary representing the game board
    """
    room_descriptions = [
        "Quiet rice fields swaying in the wind",
        "A misty bamboo forest",
        "A frozen mountain trail",
        "A burned-out village",
        "A peaceful riverside shrine",
        "A broken stone bridge",
        "A narrow forest footpath",
        "A merchant caravan camp",
        "An abandoned watchtower",
        "A muddy battlefield",
        "A hidden ninja clearing",
        "A waterfall crashing into rocks",
        "A lonely mountain cabin",
        "A cherry blossom grove",
        "A hunting trap field",
        "A ruined dojo",
        "A fog-covered valley",
        "A flooded rice terrace",
        "A bandit lookout post",
        "A rocky coastal cliff",
        "A forgotten burial mound",
        "A moonlit shrine gate",
        "A wind-swept grass plain",
        "A collapsed village well",
        "A drifting ash field from old war"
    ]

    board = {}
    for row in range(rows):
        for column in range(columns):
            random_description = random.choice(room_descriptions)
            board[(row, column)] = f"{random_description} ({row},{column})"
    return board

def describe_current_location(board, character):
    """
    Print the description of the room the player is currently in.

    :param board: a dictionary containing (row, column) tuples as keys and room descriptions as values
    :param character: a dictionary containing the character's current "x-coordinate" and "y-coordinate"
    :precondition: board must contain valid (row, column) keys and character must have valid coordinates
    :postcondition: prints a message describing the current room and its coordinates
    :return: tuple containing position and room description
    """
    position = (character["x-coordinate"], character["y-coordinate"])
    print(f"\nLocation: {position}")
    print(board[position])
    print(
        f"HP: {character['hp']}/{character['max_hp']} | "
        f"Level: {character['level']} | XP: {character['experience']}"
    )

def check_if_goal_attained(character, boss_coordinates):
    """
    Determine whether the player has reached the boss location while meeting the minimum level requirement.

    :param character: a dictionary containing character position and level
    :param boss_coordinates: a tuple representing the boss location using x and y coordinates
    :precondition: character dictionary contains keys 'x-coordinate', 'y-coordinate', and 'level'
    :postcondition: True only if player is at boss coordinates and level >= 3
    :return: True if goal is attained, otherwise False

    >>> test_character = {"x-coordinate": 9, "y-coordinate": 9, "level": 3}
    >>> check_if_goal_attained(test_character, (9, 9))
    True
    >>> test_character["level"] = 2
    >>> check_if_goal_attained(test_character, (9, 9))
    False
    """
    position = (character["x-coordinate"], character["y-coordinate"])
    return position == boss_coordinates and character["level"] >= 3

def draw_ascii_map(character, boss_coordinates):
    """
    Draw a 10x10 ASCII map showing the player's position and the boss location.

    :param character: dictionary containing the player's coordinates
    :param boss_coordinates: tuple representing the boss location using x and y coordinates
    :precondition: character dictionary contains keys 'x-coordinate' and 'y-coordinate'
    :precondition: boss_coordinates is a valid (row, column) tuple
    :postcondition: prints an ASCII representation of the game map
    :return: an ASCII map with the player and boss coordinates
    """
    print()
    for row in range(10):
        row_display = ""
        for column in range(10):
            if (row, column) == (character["x-coordinate"], character["y-coordinate"]):
                row_display += " 人 "
            elif (row, column) == boss_coordinates:
                row_display += " 帝 "
            else:
                row_display += " . "
        print(row_display)



