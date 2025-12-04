def make_character(player_name, path):
    return {
        "name": player_name,
        "path": path,
        "friend_name": "Ryūichi",
        "x_coordinate": 0,
        "y_coordinate": 0,
        "hp": 15,
        "max_hp": 15,
        "level": 1,
        "experience": 0,
        "attack_power": 3,
    }

def is_alive(character):
    return character["hp"] > 0
