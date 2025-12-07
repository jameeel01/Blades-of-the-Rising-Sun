"""
Jameel Mohammed
A01430376
"""
import pyfiglet
from user_interface import type_text_slowly

def make_character(player_name: str, path: str) -> dict:
    """
    Create and return a new player character dictionary.

    :param player_name: the name of the player
    :param path: either "samurai" or "ronin"
    :precondition: player_name is a non-empty string and path is valid
    :postcondition: a fully initialized character dictionary is created
    :return: a dictionary representing the player character

    >>> test_char = make_character("Jameel", "ronin")
    >>> test_char["name"]
    'Jameel'
    >>> test_char["path"]
    'ronin'
    >>> test_char["hp"]
    20
    >>> test_char["attack_power"]
    3
    """
    return {
        "name": player_name,
        "path": path,
        "friend_name": "Ryūichi",
        "x-coordinate": 0,
        "y-coordinate": 0,
        "hp": 20,
        "max_hp": 20,
        "level": 1,
        "experience": 0,
        "attack_power": 3,
        "bond_with_Ryūichi": 0,
        "honor": 0,
        "betrayal": False,
        "challenge_stack": []
    }

def is_alive(character):
    """
    Determine whether a character is still alive.

    :param character: a dictionary containing a hp value
    :precondition: character dictionary contains "hp"
    :postcondition: no changes are made to the character dictionary
    :return: True if hp is greater than 0, otherwise False

    >>> is_alive({"hp": 10})
    True
    >>> is_alive({"hp": 0})
    False
    >>> is_alive({"hp": -5})
    False
    """
    return character["hp"] > 0

def character_has_leveled(character):
    """
    Determine whether the character has enough experience to level up.

    :param character: a dictionary containing level and experience
    :precondition: character dictionary contains "level" and "experience"
    :postcondition: character dictionary is not modified
    :return: True if character qualifies for a level up, otherwise False

    >>> character_has_leveled({"level": 1, "experience": 5})
    True
    >>> character_has_leveled({"level": 1, "experience": 4})
    False
    >>> character_has_leveled({"level": 2, "experience": 10})
    True
    >>> character_has_leveled({"level": 2, "experience": 9})
    False
    """
    if character["level"] == 1 and character["experience"] >= 5:
        return True
    if character["level"] == 2 and character["experience"] >= 10:
        return True
    return False

def execute_level_up(character):
    """
    Increase the character's level, improve stats if eligible, and confirm if they can approach the final boss.

    :param character: a dictionary representing the player character
    :precondition: character dictionary contains "level", "hp", "max_hp", and "attack_power"
    :postcondition: character level is increased by 1, stats are improved, and hp is fully restored
    :return: the updated character dictionary
    """
    if character["level"] >= 3:
        return

    character["level"] += 1
    character["max_hp"] += 5
    character["attack_power"] += 3
    character["hp"] = character["max_hp"]

    result = pyfiglet.figlet_format("LEVEL UP!", font="SLANT")
    print(result)
    type_text_slowly(
        f"\n You are now level {character['level']}."
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