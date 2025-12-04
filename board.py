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


