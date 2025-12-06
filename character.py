import time
import sys

def type_text_slowly(text, delay=0.02):
    for character in str(text):
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def make_character(player_name, path):
    return {
        "name": player_name,
        "path": path,
        "friend_name": "Ryūichi",
        "x-coordinate": 0,
        "y-coordinate": 0,
        "hp": 20,
        "max_hp": 30,
        "level": 1,
        "experience": 0,
        "attack_power": 3,
        "bond_with_Ryūichi": 0,
        "honor": 0,
        "betrayal": False
    }

def is_alive(character):
    return character["hp"] > 0

def character_has_leveled(character):
    if character["level"] == 1 and character["experience"] >= 5:
        return True
    if character["level"] == 2 and character["experience"] >= 10:
        return True
    return False

def execute_level_up(character):
    if character["level"] >= 3:
        return

    character["level"] += 1
    character["max_hp"] += 5
    character["attack_power"] += 3
    character["hp"] = character["max_hp"]

    type_text_slowly(
        f"\nLevel Up! You are now level {character['level']}."
        f" Max HP: {character['max_hp']}, Attack: {character['attack_power']}\n"
    )

    if character["level"] == 3:
        type_text_slowly("\nA strange stillness settles around you...")
        type_text_slowly("Your body feels stronger. Your blade feels lighter.")
        type_text_slowly("You know, without doubt — you are ready.\n")

        if character["path"] == "ronin":
            type_text_slowly("The road to the palace opens before you.")
            type_text_slowly("The Emperor's fate now lies within your reach.\n")
        else:
            type_text_slowly("The path to the palace is finally clear.")
            type_text_slowly("The Emperor will soon need your blade's protection.\n")