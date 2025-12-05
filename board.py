import random


def make_board(rows, columns):
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
    position = (character["x-coordinate"], character["y-coordinate"])
    print(f"\nLocation: {position}")
    print(board[position])
    print(
        f"HP: {character['hp']}/{character['max_hp']} , "
        f"Level: {character['level']} , XP: {character['experience']}"
    )

def check_if_goal_attained(character, boss_coordinates):
    position = (character["x-coordinate"], character["y-coordinate"])
    return position == boss_coordinates and character["level"] >= 3

def draw_ascii_map(character, boss_coordinates):
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



