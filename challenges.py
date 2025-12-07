"""
Jameel Mohammed
A01430376
"""
from itertools import cycle
import random
from user_interface import (
    final_boss_intro_samurai,
    final_boss_outro_samurai,
    final_boss_intro_ronin,
    emperor_death_scene,
    betrayal_confrontation_intro,
    betrayal_spared_scene,
    betrayal_duel_scene,
    rebuild_scene,
    abandonment_scene,
    print_final_duel_banner,
    type_text_slowly
)

def ryuichi_present(character):
    """
    Determine whether Ryūichi is currently accompanying the player.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains a "path" key
    :postcondition: the character's path is determined
    :return: character path in dictionary updates to "ronin"
    """
    return character["path"] == "ronin"

def challenge_stack(character):
    """
    Create and shuffle a non-repeating stack of challenges for the player.

    :param character: a dictionary representing the player's character
    :precondition: character is a valid dictionary
    :postcondition: character gains a shuffled "challenge_stack" list
    :return: an updated character dictionary
    """
    challenge = cycle([
        "combat", "riddle", "moral", "traveler",
        "duel", "sacrifice", "gamble",
        "hostage", "wounded_soldier",
        "execution", "duel_of_honor",
        "burning_village", "shrine",
        "ambush", "merchant", "healer",
        "spirit", "feast", "thief",
        "bridge", "blessing", "training",
        "pilgrim", "assassin"
    ])
    character["challenge_stack"] = challenge

def execute_challenge(character):
    """
    Execute a randomly selected, non-repeating challenge from the character's challenge stack list.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains a valid "challenge_stack"
    :precondition: character dictionary can add a valid "challenge_stack"
    :postcondition: one challenge is removed from the stack list
    :return: execute a challenge from the dictionary stack list
    """
    if len(character["challenge_stack"]) == 0:
        challenge_stack(character)

    challenge_type = character["challenge_stack"].pop()

    if challenge_type == "combat":
        combat_challenge(character)
    elif challenge_type == "riddle":
        riddle_challenge(character)
    elif challenge_type == "shrine":
        shrine_challenge(character)
    elif challenge_type == "moral":
        moral_challenge(character)
    elif challenge_type == "ambush":
        ambush_challenge(character)
    elif challenge_type == "traveler":
        traveler_challenge(character)
    elif challenge_type == "gamble":
        gamble_challenge(character)
    elif challenge_type == "merchant":
        merchant_challenge(character)
    elif challenge_type == "healer":
        healer_challenge(character)
    elif challenge_type == "spirit":
        spirit_challenge(character)
    elif challenge_type == "feast":
        feast_challenge(character)
    elif challenge_type == "thief":
        thief_challenge(character)
    elif challenge_type == "bridge":
        bridge_challenge(character)
    elif challenge_type == "blessing":
        blessing_challenge(character)
    elif challenge_type == "training":
        training_challenge(character)
    elif challenge_type == "pilgrim":
        pilgrim_challenge(character)
    elif challenge_type == "assassin":
        assassin_challenge(character)
    elif challenge_type == "hostage":
        hostage_challenge(character)
    elif challenge_type == "wounded_soldier":
        wounded_soldier_challenge(character)
    elif challenge_type == "execution":
        execution_challenge(character)
    elif challenge_type == "duel_of_honor":
        duel_of_honor_challenge(character)
    elif challenge_type == "burning_village":
        burning_village_challenge(character)
    else:
        sacrifice_challenge(character)


def combat_challenge(character):
    """
    Execute a combat encounter against a random enemy and choose from a list of inputs.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains hp, max_hp, attack_power, and level
    :postcondition: character hp and experience change based on choice
    :return: the updated character dictionary
    """
    foes = [
        {"name": "lost child", "min_level": 1},
        {"name": "wild boar", "min_level": 1},
        {"name": "mountain thief", "min_level": 2},
        {"name": "rogue samurai", "min_level": 3},
        {"name": "seductive ninja", "min_level": 3}
    ]
    available_foes = [
        foe for foe in foes
        if foe["min_level"] <= character["level"]
    ]
    enemy = random.choice(available_foes)
    enemy_hp = 6 + (character["level"] * 3)

    type_text_slowly(f"\nA {enemy} challenges you to battle!")

    while enemy_hp > 0 and character["hp"] > 0:
        print(f"\nYour HP: {character['hp']}/{character['max_hp']} | {enemy.title()} HP: {enemy_hp}")
        print("[1] Attack")
        print("[2] Defend")
        print("[3] Run away\n")

        choice = input("Your move: ").strip()
        while choice not in ["1", "2", "3"]:
            choice = input("Invalid choice. Enter 1, 2, or 3: ").strip()

        player_roll = random.randint(1, 10)
        enemy_roll = random.randint(1, 10)

        if choice == "1":
            if player_roll >= enemy_roll:
                enemy_hp -= character["attack_power"]
                type_text_slowly(f"\nYou strike the {enemy} for {character["attack_power"]} damage!")
            else:
                damage = 2 * character["level"]
                character["hp"] -= damage
                type_text_slowly(f"\nThe {enemy} hits you for {damage} damage!")
                type_text_slowly(f"\nYou lose {damage} HP!")
                print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "2":
            heal = 2
            if character["hp"] == character["max_hp"]:
                type_text_slowly(f"You block {enemy}'s attack successfully.")
            else:
                character["hp"] += heal
                type_text_slowly(f"You block and drink a health potion. You heal for {heal} HP")
            print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "3":
            if random.randint(1, 10) >= 4:
                type_text_slowly(f"\nYou are being watched by the locals and can't run! The {enemy} strikes you!")
                type_text_slowly(f"\nYou lose 1 HP!")
                character["hp"] -= 1
            else:
                type_text_slowly("\nYou cover your face and flee!")
                break

    if enemy_hp <= 0:
        type_text_slowly(f"\nYou have defeated the {enemy}.")
        character["experience"] += 1
    else:
        type_text_slowly("\nYou retreat from battle.")

def riddle_challenge(character):
    """
    Present a riddle that rewards experience for a correct answer.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains hp, experience, and bond_with_Ryūichi
    :postcondition: character hp, experience, or bond change based on choice
    :return: the updated character dictionary
    """
    type_text_slowly("\nA wandering monk stops you.")
    type_text_slowly("What walks on four legs in the morning, two at noon, and three in the evening?")
    print("[1] A dragon")
    print("[2] A human")
    print("[3] A wolf")
    print("[4] A mouse")

    answer = input("Your choice: ").strip()
    while answer not in ["1", "2", "3", "4"]:
        answer = input("Invalid choice. Enter 1, 2, 3, or 4: ").strip()

    if answer == "2":
        character["experience"] += 1
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] += 1
            type_text_slowly("\nCorrect. Ryūichi nods in quiet approval.")
        else:
            type_text_slowly("\nCorrect. You feel your confidence grow.")
    else:
        character["hp"] -= 2
        type_text_slowly("\nThe monk stabs you for insulting his intelligence. You lose 2 HP.")
        print(f"HP: {character['hp']}/{character['max_hp']}")

def shrine_challenge(character):
    """
    Present a shrine encounter that may restore health.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains hp, max_hp, and level
    :postcondition: character hp changes based on choice
    :return: the updated character dictionary
    """
    type_text_slowly("\nYou discover a glowing shrine.")
    print("[1] Drink from the shrine")
    print("[2] Leave it alone")

    choice = input("Your choice: ").strip()
    while choice not in ["1", "2"]:
        choice = input("Invalid choice. Enter 1 or 2: ").strip()

    if choice == "1":
        heal = 1 * character["level"]
        if character["hp"] == character["max_hp"]:
            type_text_slowly("\nThis shrine's water tastes like moldy feet and old coins.")
        else:
            character["hp"] = min(character["hp"] + heal, character["max_hp"])
            type_text_slowly(f"\nYou feel warmth. You gain {heal}HP.")
            print(f"HP: {character['hp']}/{character['max_hp']}")
    else:
        print("\nYou bow and walk away.")

def moral_challenge(character):
    """
    Present a moral decision involving a starving thief.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains honor, experience, and bond_with_Ryūichi
    :postcondition: character honor, experience, or bond change based on choice
    :return: the updated character dictionary
    """
    type_text_slowly("\nA starving thief steals rice from a farmer.")
    print("[1] Kill the thief")
    print("[2] Let the thief go")
    print("[3] Give your own food\n")

    choice = input("Your choice: ").strip()
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Enter 1, 2, or 3: ").strip()

    if choice == "1":
        character["experience"] += 1
        character["honor"] -= 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 1
            type_text_slowly("\nYou kill the thief. Ryūichi shakes his head in dismay.")
        else:
            type_text_slowly("\nYou carry out the execution without hesitation.")
    elif choice == "2":
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] += 1
            type_text_slowly("\nYou spare the thief but give the rice back to the farmer. Ryūichi gives the thief some food.")
        else:
            type_text_slowly("\nYou let the thief flee into the night. The farmer screams at you.")
    else:
        character["honor"] += 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] += 2
            type_text_slowly("\nRyūichi smiles at your compassion.")
            type_text_slowly(f"\"We will find dinner elsewhere don't worry {character["name"]}\".")
        else:
            type_text_slowly("\nYou give your last food away to the thief and walk on in silence.")

def ambush_challenge(character):
    """
    Trigger a sudden bandit ambush that damages the player.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains hp and max_hp
    :postcondition: character hp is reduced
    :return: the updated character dictionary
    """
    type_text_slowly("\nBandits leap from the trees!")
    damage = random.randint(2,4)
    character["hp"] = max(character["hp"] - damage, 0)
    type_text_slowly(f"\nYou escape but lose {damage} HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def traveler_challenge(character):
    """
    Handle an encounter with a lost traveler asking for money.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains honor, experience, and bond_with_Ryūichi
    :postcondition: character honor, experience, and bond_with_Ryūichi change based on choice
    :return: the updated character dictionary
    """
    type_text_slowly("\nA lost traveler asks for money.")
    print("[1] Help")
    print("[2] Ignore")
    choice = input("Your choice: ").strip()
    while choice not in ["1","2"]:
        choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        character["experience"] += 1
        character["honor"] += 1
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] += 1
            type_text_slowly("\nYou give the traveler a few coins. Ryūichi is deeply moved.")
        else:
            type_text_slowly("\nYou give the traveler a few coins. The traveler bows deeply in gratitude.")
    else:
        character["honor"] -= 1
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 1
            type_text_slowly("\nYou pretend you hear nothing.")
            type_text_slowly("Ryūichi gives the traveler a few coins then glares at you in disappointment.")
        else:
            type_text_slowly("\nYou leave the traveler behind without looking back.")

def gamble_challenge(character):
    """
     Perform a gambling encounter with random rewards or penalties.

     :param character: a dictionary representing the player's character
     :precondition: character dictionary contains hp and experience
     :postcondition: character hp decreased or experience increased
     :return: the updated character dictionary
     """
    type_text_slowly("\nA dice gambler challenges you.")
    roll = random.randint(1,10)
    if roll >= 6:
        character["experience"] += 1
        type_text_slowly("\nYou win the gamble. You gain 1 experience.")
    else:
        character["hp"] = max(character["hp"] - 2, 0)
        type_text_slowly("\nYou lose and take 2 HP damage.")
        print(f"HP: {character['hp']}/{character['max_hp']}")


def merchant_challenge(character):
    """
    Restore a small amount of health through a merchant interaction.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains hp and max_hp
    :postcondition: character hp is increased
    :return: the updated character dictionary
    """
    type_text_slowly("\nA merchant overcharges you for supplies.")
    heal = 2
    character["hp"] = min(character["hp"] + heal, character["max_hp"])
    type_text_slowly(f"\nYou recover {heal} HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def healer_challenge(character):
    """
    Heal the player by a fixed amount through a wandering healer.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains hp and max_hp
    :postcondition: character hp increases but does not exceed max_hp
    :return: the updated character dictionary
    """
    type_text_slowly("\nA wandering healer treats your wounds.")
    heal = 3
    character["hp"] = min(character["hp"] + heal, character["max_hp"])
    type_text_slowly(f"\nYou gain {heal} HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def spirit_challenge(character):
    """
    Resolve an encounter with a spirit based on the player's honor stat.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains honor, hp, and experience
    :postcondition: character hp decreased or experience increased
    :return: the updated character dictionary
    """
    type_text_slowly("\nA spirit blocks your path.")
    if character["honor"] >= 3:
        character["experience"] += 2
        type_text_slowly("\nThe spirit bows and grants you power. You gain 2 experience.")
    elif character["honor"] <= -2:
        character["hp"] = max(character["hp"] - 2, 0)
        type_text_slowly("\nThe spirit recoils from your darkness. You lose 2 HP.")
    else:
        type_text_slowly("\nThe spirit watches silently and vanishes.")

def feast_challenge(character):
    """
    Restore health to the player through a village feast.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains hp and max_hp
    :postcondition: character hp is increased
    :return: the updated character dictionary
    """
    type_text_slowly("\nA village offers you a feast.")
    character["hp"] = min(character["hp"] + 3, character["max_hp"])
    type_text_slowly("\nYou recover 3 HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def thief_challenge(character):
    """
    Reduce player's experience due to a theft at night.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains experience
    :postcondition: character experience is reduced
    :return: the updated character dictionary
    """
    type_text_slowly("\nA thief steals from you in the night.")
    character["experience"] -= 1
    type_text_slowly("\nYou lose 1 experience.")

def bridge_challenge(character):
    """
    Determine whether the player safely crosses a broken bridge.

    :param character: a dictionary representing the player's character
    :precondition: character contains hp
    :postcondition: character hp remains the same or reduced
    :return: the updated character dictionary
    """
    type_text_slowly("\nA broken bridge blocks your path.")
    if random.randint(1,10) >= 5:
        type_text_slowly("\nYou cross safely.")
    else:
        character["hp"] = max(character["hp"] - 2, 0)
        type_text_slowly("\nYou fall and lose 2 HP.")
        print(f"HP: {character['hp']}/{character['max_hp']}")


def blessing_challenge(character):
    """
    Increase the player's experience through a monk's blessing.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains experience
    :postcondition: character experience increases
    :return: the updated character dictionary
    """
    type_text_slowly("\nA monk blesses your journey.")
    character["experience"] += 1
    type_text_slowly("\nYou gain 1 experience.")
    print(f"Experience: {character['experience']}")


def training_challenge(character):
    """
    Increase experience through brief training.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains experience
    :postcondition: character experience increases
    :return: the updated character dictionary
    """
    type_text_slowly("\nA veteran trains you briefly.")
    character["experience"] += 2
    type_text_slowly("\nYou gain 2 experience.")

def pilgrim_challenge(character):
    """
    Reward experience through wisdom shared by a pilgrim.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains experience
    :postcondition: character experience increases
    :return: the updated character dictionary
    """
    type_text_slowly("\nA pilgrim shares wisdom.")
    character["experience"] += 1
    type_text_slowly("\nYou gain 1 experience.")

def assassin_challenge(character):
    """
    Apply random damage from an assassin ambush.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains hp
    :postcondition: character hp decreases
    :return: the updated character dictionary
    """
    type_text_slowly("\nAn assassin strikes from the shadows!")
    damage = random.randint(3,5)
    character["hp"] = max(character["hp"] - damage, 0)
    type_text_slowly(f"\nYou lose {damage} HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def sacrifice_challenge(character):
    """
    Allow the player to sacrifice health in exchange for power or resist temptation.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains hp, honor, attack_power, and bond_with_Ryūichi
    :postcondition: character hp, honor, attack_power, and bond_with_Ryūichi change based on choice
    :return: the updated character dictionary
    """
    type_text_slowly("\nA shrine demands sacrifice.")
    print("[1] Offer blood")
    print("[2] Refuse")
    choice = input("Your choice: ").strip()
    while choice not in ["1","2"]:
        choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        character["hp"] -= 2
        character["attack_power"] += 2
        character["experience"] += 2
        character["honor"] -= 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 1
            type_text_slowly("\nPower answers your blood. You lose 2 HP but gain 2 attack. Ryūichi turns away in silence.")
        else:
            type_text_slowly("\nDark power floods your veins. You lose 2 HP but gain 2 attack.")
        print(f"HP: {character['hp']}/{character['max_hp']} | Attack power: {character['attack_power']}")
    else:
        character["honor"] += 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] += 1
            type_text_slowly("\nYou refuse the dark power. Ryūichi nods with respect.")
        else:
            type_text_slowly("\nYou resist the temptation and walk on.")


def hostage_challenge(character):
    """
    Resolve a hostage situation through combat, negotiation, or abandonment.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains honor, experience, and bond_with_Ryūichi
    :postcondition: character honor, experience, and bond_with_Ryūichi change based on choice
    :return: the updated character dictionary
    """
    type_text_slowly("\nBandits hold a villager at knifepoint.")
    print("[1] Attack immediately")
    print("[2] Try to negotiate")
    print("[3] Walk away")

    choice = input("Your choice: ").strip()
    while choice not in ["1","2","3"]:
        choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        if random.randint(1, 10) >= 6:
            character["experience"] += 2
            character["honor"] += 1
            if ryuichi_present(character):
                character["bond_with_Ryūichi"] += 1
                type_text_slowly("\nYou save the hostage. Ryūichi exhales in relief.")
            else:
                type_text_slowly("\nYou strike fast and save the hostage.")
        else:
            character["experience"] += 1
            character["honor"] -= 1
            if ryuichi_present(character):
                character["bond_with_Ryūichi"] += 1

                type_text_slowly("\nYou attempt to save the villager but you do not make it in time.")
                type_text_slowly("You viciously kill the bandits in a fit of rage.")
                type_text_slowly("Ryūichi rubs your back and consoles you.")
            else:
                type_text_slowly("\nYou attempt to save the villager but you do not make it in time.")
                type_text_slowly("You viciously kill the bandits in a fit of rage.")
    elif choice == "2":
        character["honor"] += 1
        character["experience"] += 1
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] += 1
            type_text_slowly("\nYou explain to the bandits they will receive death if they persist.")
            type_text_slowly("The bandits try to run but you and Ryūichi catch them. You leave them tied up for the villagers")
        else:
            type_text_slowly("\nYou explain to the bandits they will receive death if they persist.")
            type_text_slowly("The bandits run away.")
    else:
        character["honor"] -= 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 1
            type_text_slowly("\nYou decide to leave them to their fate.")
            type_text_slowly("Ryūichi looks at you in frustration and steps in to save the villager.")
        else:
            type_text_slowly("\nYou decide to leave them to their fate.")

def wounded_soldier_challenge(character):
    """
    Present a moral decision regarding a wounded soldier.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains honor and bond_with_Ryūichi
    :postcondition: character honor or bond change based on choice
    :return: the updated character dictionary
    """
    type_text_slowly("\nA wounded soldier begs for help.")
    print("[1] Heal him")
    print("[2] End his suffering")
    print("[3] Ignore him")

    choice = input("Your choice: ").strip()
    while choice not in ["1","2","3"]:
        choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        character["honor"] += 1
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] += 2
            type_text_slowly("\nYou wrap the soldier's wounds and provide him with medicine.")
            type_text_slowly("Ryūichi watches with respect.")
        else:
            type_text_slowly("\nYou wrap the soldier's wounds and provide him with medicine.")
            type_text_slowly("The soldier thanks you with trembling hands.")
    elif choice == "2":
        character["honor"] -= 1
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 1
            type_text_slowly("\nYou kill the wounded soldier. Ryūichi turns away, shaken.")
        else:
            type_text_slowly("\nYou grant him a quick death.")
    else:
        character["honor"] -= 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 2
            type_text_slowly("\nYou leave him behind to suffer. Ryūichi yells at you and starts helping the soldier.")
        else:
            type_text_slowly("\nYou leave him behind to suffer.")

def execution_challenge(character):
    """
    Handle a public execution event with multiple moral outcomes.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains honor, experience, and bond_with_Ryūichi
    :postcondition: character honor, experience, and bond_with_Ryūichi change based on choice
    :return: the updated character dictionary
    """
    type_text_slowly("\nAn execution of murderous child is underway in the village square.")
    print("[1] Intervene")
    print("[2] Observe silently")
    print("[3] Aid the executioner")

    choice = input("Your choice: ").strip()
    while choice not in ["1", "2", "3"]:
        choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        character["experience"] += 1
        if ryuichi_present(character):
            character["honor"] += 2
            character["bond_with_Ryūichi"] += 1
            type_text_slowly("\nYou disrupt the execution as Ryūichi fights the samurai beside you.")
            type_text_slowly("The child decides to join the ronin.")
        else:
            character["honor"] -= 1
            type_text_slowly("\nYou disrupt the execution as chaos erupts. The child runs away while killing villagers.")
    elif choice == "2":
        character["honor"] -= 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 1
            type_text_slowly("\nYou say nothing as the blade falls. Ryūichi turns away in anger.")
        else:
            type_text_slowly("\nYou say nothing as the blade falls.")
    else:
        character["honor"] -= 3
        character["experience"] += 1
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 2
            type_text_slowly("\nYou gleefully help the executioner. Ryūichi looks at you in disbelief.")
        else:
            type_text_slowly("\nYou coldly assist the execution without question.")

def duel_of_honor_challenge(character):
    """
    Resolve a public duel that tests the player's honor.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains honor, experience, and bond_with_Ryūichi
    :postcondition: character honor, experience, and bond_with_Ryūichi change based on choice
    :return: the updated character dictionary
    """
    type_text_slowly("\nA proud warrior challenges you publicly.")
    print("[1] Accept honorably")
    print("[2] Fight dirty")
    print("[3] Refuse")

    choice = input("Your choice: ").strip()
    while choice not in ["1", "2", "3"]:
        choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        character["experience"] += 2
        character["honor"] += 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] += 1
            type_text_slowly("\nYou best the warrior and he begs for mercy.")
            type_text_slowly("Ryūichi holds your fist high in the air.")
        else:
            type_text_slowly("\nYou best the warrior and he begs for mercy.")
        print(f"You gain 2 experience.")
    elif choice == "2":
        character["experience"] += 1
        character["honor"] -= 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 1
            type_text_slowly("\nYou shove dirt in the warriors face then stab him in the groin.")
            type_text_slowly("Ryūichi hangs his head in shame.")
        else:
            type_text_slowly("\nYou shove dirt in the warriors face then stab him in the groin.")
        print(f"You gain 1 experience.")
    else:
        character["honor"] -= 1
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 1
            type_text_slowly("\nYou walk away as the crowd jeers. Ryūichi looks at you in disappointment.")
        else:
            type_text_slowly("\nYou walk away as the crowd jeers.")

def burning_village_challenge(character):
    """
    Present a burning village scenario with multiple outcomes.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains honor, experience, and bond_with_Ryūichi
    :postcondition: character honor, experience, and bond_with_Ryūichi change based on choice
    :return: the updated character dictionary
    """
    type_text_slowly("\nA village burns under attack!")
    print("[1] Save villagers")
    print("[2] Chase attackers")
    print("[3] Scavenge supplies from the burning village")

    choice = input("Your choice: ").strip()
    while choice not in ["1","2","3"]:
        choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        character["honor"] += 2
        character["experience"] += 1
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] += 1
            type_text_slowly("\nYou rescue villagers as Ryūichi covers your retreat.")
        else:
            type_text_slowly("\nYou pull villagers from the flames alone.")
    elif choice == "2":
        character["experience"] += 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 1
            type_text_slowly("\nYou cut down fleeing attackers through smoke and fire. Ryūichi runs to save the villagers.")
            print(f"You gain 2 experience.")
        else:
            type_text_slowly("\nAs the village burns, you cut down fleeing attackers through smoke and fire.")
            print(f"You gain 2 experience.")
    else:
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 2
            character["honor"] -= 2
            type_text_slowly("\nRyūichi shoves you to the ground as you try and steal from the burning village.")
        else:
            character["honor"] -= 2
            character["experience"] += 1
            type_text_slowly("\nYou scavenge what supplies you can from the burning ruins and move on.")
            print(f"You gain 1 experience.")

def boss_fight(character, boss_name):
    """
    Execute the final boss combat sequence.

    :param character: a dictionary representing the player's character
    :param boss_name: string name of the boss
    :precondition: character dictionary contains hp, max_hp, level, and attack_power
    :postcondition: character hp changes based on choice
    :return: True if the player survives the fight, False otherwise
    """
    boss_hp = 20 + (character["level"] * 5)

    while boss_hp > 0 and character["hp"] > 0:
        print(f"\nYour HP: {character['hp']}/{character['max_hp']} | {boss_name} HP: {boss_hp}")
        print("[1] Attack")
        print("[2] Defend")
        print("[3] Risky Strike\n")

        choice = input("Your move: ").strip()
        while choice not in ["1", "2", "3"]:
            choice = input("Invalid choice. Enter 1, 2, or 3: ").strip()

        player_roll = random.randint(1, 5)
        boss_roll = random.randint(1, 10)

        if choice == "1":
            if player_roll >= boss_roll:
                damage = character["attack_power"]
                boss_hp -= damage
                type_text_slowly(f"You strike for {damage} damage.")
            else:
                damage = 3 * character["level"]
                character["hp"] -= damage
                type_text_slowly(f"You are struck for {damage} damage.")
                print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "2":
            if random.randint(1, 10) >= 3:
                heal = 5
                if character["hp"] == character["max_hp"]:
                    type_text_slowly(f"You block {boss_name}'s attack successfully.")
                else:
                    character["hp"] += heal
                    type_text_slowly(f"You block and drink a health potion. You heal for {heal} HP")
                print(f"HP: {character['hp']}/{character['max_hp']}")
            else:
                damage = random.randint(1, 5)
                character["hp"] -= damage
                type_text_slowly(f"You try to block {boss_name}'s incoming attack.")
                type_text_slowly(f"You feel pain under {boss_name}'s strength.")
                type_text_slowly(f"You lose {damage}HP.")
                print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "3":
            if random.randint(1, 10) >= 6:
                damage = character["attack_power"] * 2
                boss_hp -= damage
                type_text_slowly(f"Your all-out strike deals {damage} damage.")
            else:
                damage = 4 * character["level"]
                character["hp"] -= damage
                type_text_slowly(f"Your all-out strike gets parried. You take {damage} damage.")
                print(f"HP: {character['hp']}/{character['max_hp']}")
    return character["hp"] > 0

def final_boss_story(character):
    """
    Execute the full final boss narrative and combat sequence.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains path, bond_with_Ryūichi, and betrayal
    :postcondition: final story outcome is displayed and game ending is determined
    :return: True if the player completes the final boss sequence successfully, False otherwise
    """
    if character["path"] == "samurai":
        boss = character["friend_name"]

        final_boss_intro_samurai()
        print_final_duel_banner()
        result = boss_fight(character, boss)

        if result:
            final_boss_outro_samurai()
        return result
    else:
        boss = "the Emperor"
        final_boss_intro_ronin()
        print_final_duel_banner()
        emperor_defeated = boss_fight(character, boss)

        if not emperor_defeated:
            return False
        emperor_death_scene()

        if character["betrayal"]:
            betrayal_confrontation_intro()
            if character["bond_with_Ryūichi"] >= 3:
                betrayal_spared_scene()
            else:
                betrayal_duel_scene()
        else:
            if character["bond_with_Ryūichi"] >= 3:
                rebuild_scene()
            else:
                abandonment_scene()
        return True
