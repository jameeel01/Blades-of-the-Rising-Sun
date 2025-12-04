import random


def check_for_challenge():
    number = random.randint(1, 10)
    if number <= 4:
        return True
    else:
        return False


def execute_challenge(character):
    challenge_type = random.choice(
        ["combat", "riddle", "shrine", "moral"]
    )

    if challenge_type == "combat":
        combat_challenge(character)
    elif challenge_type == "riddle":
        riddle_challenge(character)
    elif challenge_type == "shrine":
        shrine_challenge(character)
    elif challenge_type == "moral":
        moral_challenge(character)
