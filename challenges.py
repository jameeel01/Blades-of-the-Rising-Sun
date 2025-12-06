import random
import time
import sys

def type_text_slowly(text, delay=0.02):
    for character in str(text):
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def execute_challenge(character):
    challenge_type = random.choice([
        "combat","riddle","shrine","moral",
        "ambush","traveler","gamble","storm","merchant",
        "healer","duel","trap","spirit","feast",
        "thief","boar_charge","archer","bridge",
        "fire","blessing","curse","training",
        "pilgrim","assassin", "sacrifice"
    ])

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
    elif challenge_type == "storm":
        storm_challenge(character)
    elif challenge_type == "merchant":
        merchant_challenge(character)
    elif challenge_type == "healer":
        healer_challenge(character)
    elif challenge_type == "duel":
        duel_challenge(character)
    elif challenge_type == "trap":
        trap_challenge(character)
    elif challenge_type == "spirit":
        spirit_challenge(character)
    elif challenge_type == "feast":
        feast_challenge(character)
    elif challenge_type == "thief":
        thief_challenge(character)
    elif challenge_type == "boar_charge":
        boar_charge_challenge(character)
    elif challenge_type == "archer":
        archer_challenge(character)
    elif challenge_type == "bridge":
        bridge_challenge(character)
    elif challenge_type == "fire":
        fire_challenge(character)
    elif challenge_type == "blessing":
        blessing_challenge(character)
    elif challenge_type == "curse":
        curse_challenge(character)
    elif challenge_type == "training":
        training_challenge(character)
    elif challenge_type == "pilgrim":
        pilgrim_challenge(character)
    elif challenge_type == "assassin":
        assassin_challenge(character)
    else:
        sacrifice_challenge(character)


def combat_challenge(character):
    foes = ["lost child", "rogue samurai", "wild boar", "mountain thief", "seductive ninja"]
    enemy = random.choice(foes)
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

        player_roll = random.randint(1, 10) + character["attack_power"]
        enemy_roll = random.randint(1, 10)

        if choice == "1":
            if player_roll >= enemy_roll:
                enemy_hp -= 3
                type_text_slowly(f"You strike the {enemy} for 3 damage!")
            else:
                character["hp"] -= 3
                type_text_slowly(f"The {enemy} hits you for 3 damage!")
                print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "2":
            character["hp"] -= 1
            type_text_slowly("You defend but still take 1 damage.")
            print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "3":
            if random.randint(1, 10) >= 4:
                type_text_slowly(f"You are being watched by the locals and can't run! The {enemy} strikes you!")
                character["hp"] -= 1
            else:
                type_text_slowly("You cover your face and flee!")
                break

    if enemy_hp <= 0:
        type_text_slowly(f"\nYou have defeated the {enemy}.")
        character["experience"] += 1
        type_text_slowly(f"Experience increased to {character['experience']}")
    else:
        type_text_slowly("\nYou retreat from battle.")

def riddle_challenge(character):
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
        character["bond_with_Ryūichi"] += 1
        type_text_slowly("Correct. Ryūichi nods in quiet approval.")
        print(f"Experience: {character['experience']}")
    else:
        character["hp"] -= 2
        type_text_slowly("The monk stabs you for insulting his intelligence. You lose 2 HP.")
        print(f"HP: {character['hp']}/{character['max_hp']}")

def shrine_challenge(character):
    type_text_slowly("\nYou discover a glowing shrine.")
    print("[1] Drink from the shrine")
    print("[2] Leave it alone")

    choice = input("Your choice: ").strip()
    while choice not in ["1", "2"]:
        choice = input("Invalid choice. Enter 1 or 2: ").strip()

    if choice == "1":
        heal = random.randint(1, 3)
        if character["hp"] == character["max_hp"]:
            type_text_slowly("This shrine's water tastes like moldy feet and old coins.")
        else:
            character["hp"] = min(character["hp"] + heal, character["max_hp"])
            type_text_slowly(f"You feel warmth. HP restored by {heal}.")
            print(f"HP: {character['hp']}/{character['max_hp']}")
    else:
        print("You bow and walk away.")

def moral_challenge(character):
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
        type_text_slowly("You kill the thief and Ryūichi shakes his head in dismay. You lose honor but gain 1 experience.")
    elif choice == "2":
        character["bond_with_Ryūichi"] += 1
        type_text_slowly("You spare the thief. Ryūichi quietly nods in approval.")
    elif choice == "3":
        character["honor"] += 2
        character["bond_with_Ryūichi"] += 2
        type_text_slowly("You give your food away. Ryūichi puts his hand on your shoulder and smiles.")

    print(f"Experience: {character['experience']}")

def ambush_challenge(character):
    type_text_slowly("\nBandits leap from the trees!")
    damage = random.randint(2,4)
    character["hp"] -= damage
    type_text_slowly(f"You escape but lose {damage} HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def traveler_challenge(character):
    type_text_slowly("\nA lost traveler asks for protection.")
    print("[1] Help")
    print("[2] Ignore")
    choice = input("Your choice: ").strip()
    while choice not in ["1","2"]:
        choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        character["experience"] += 1
        character["honor"] += 1
        character["bond_with_Ryūichi"] += 1
        type_text_slowly("You guide them safely. Ryūichi smiles at your compassion.")
        print(f"Experience: {character['experience']}")
    else:
        character["honor"] -= 1
        character["bond_with_Ryūichi"] -= 1
        type_text_slowly("You turn your back on the helpless traveler. Ryūichi storms off in anger")

def gamble_challenge(character):
    type_text_slowly("\nA dice gambler challenges you.")
    roll = random.randint(1,10)
    if roll >= 6:
        character["experience"] += 1
        type_text_slowly("You win the gamble. You gain 1 experience.")
    else:
        character["hp"] -= 2
        type_text_slowly("You lose and take 2 HP damage.")
        print(f"HP: {character['hp']}/{character['max_hp']}")

def storm_challenge(character):
    type_text_slowly("\nA violent storm batters you.")
    character["hp"] -= 1
    type_text_slowly("You lose 1 HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def merchant_challenge(character):
    type_text_slowly("\nA merchant overcharges you for supplies.")
    character["hp"] += 1 if character["hp"] < character["max_hp"] else 0
    type_text_slowly("You recover 1 HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def healer_challenge(character):
    type_text_slowly("\nA wandering healer treats your wounds.")
    heal = 2
    character["hp"] = min(character["hp"] + heal, character["max_hp"])
    type_text_slowly(f"You gain {heal} HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def duel_challenge(character):
    type_text_slowly("\nA warrior challenges you to a duel.")
    if random.randint(1,10) >= 6:
        character["experience"] += 2
        type_text_slowly("You win the duel! You gain 2 experience.")
        print(f"Experience: {character['experience']}")
    else:
        character["hp"] -= 3
        type_text_slowly("You are wounded in the duel. You lose 3 HP.")
        print(f"HP: {character['hp']}/{character['max_hp']}")

def trap_challenge(character):
    type_text_slowly("\nYou step into a hidden trap.")
    character["hp"] -= 2
    type_text_slowly("You lose 2 HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def spirit_challenge(character):
    type_text_slowly("\nA restless spirit appears.")
    if random.randint(1,10) >= 5:
        character["experience"] += 1
        type_text_slowly("The spirit blesses you. You gain 1 experience.")
        print(f"Experience: {character['experience']}")
    else:
        character["hp"] -= 2
        type_text_slowly("The spirit drains your life. You lose 2 HP.")
        print(f"HP: {character['hp']}/{character['max_hp']}")

def feast_challenge(character):
    type_text_slowly("\nA village offers you a feast.")
    character["hp"] = min(character["hp"] + 3, character["max_hp"])
    type_text_slowly("You recover 3 HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def thief_challenge(character):
    type_text_slowly("\nA thief steals from you in the night.")
    character["experience"] -= 1
    type_text_slowly("You lose 1 experience.")
    print(f"Experience: {character['experience']}")

def boar_charge_challenge(character):
    type_text_slowly("\nA wild boar charges!")
    damage = random.randint(2,4)
    character["hp"] -= damage
    type_text_slowly(f"You take {damage} HP damage.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def archer_challenge(character):
    type_text_slowly("\nAn archer fires from the hills.")
    character["hp"] -= 2
    type_text_slowly("You lose 2 HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def bridge_challenge(character):
    type_text_slowly("\nA broken bridge blocks your path.")
    if random.randint(1,10) >= 5:
        type_text_slowly("You cross safely.")
    else:
        character["hp"] -= 2
        type_text_slowly("You fall and lose 2 HP.")
        print(f"HP: {character['hp']}/{character['max_hp']}")

def fire_challenge(character):
    type_text_slowly("\nA sudden fire engulfs the path.")
    character["hp"] -= 3
    type_text_slowly("You lose 3 HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def blessing_challenge(character):
    type_text_slowly("\nA monk blesses your journey.")
    character["experience"] += 1
    type_text_slowly("You gain 1 experience.")
    print(f"Experience: {character['experience']}")

def curse_challenge(character):
    type_text_slowly("\nA dark curse weakens you.")
    character["hp"] -= 2
    type_text_slowly("You lose 2 HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def training_challenge(character):
    type_text_slowly("\nA veteran trains you briefly.")
    character["experience"] += 2
    type_text_slowly("You gain 2 experience.")
    print(f"Experience: {character['experience']}")

def pilgrim_challenge(character):
    type_text_slowly("\nA pilgrim shares wisdom.")
    character["experience"] += 1
    type_text_slowly("You gain 1 experience.")
    print(f"Experience: {character['experience']}")

def assassin_challenge(character):
    type_text_slowly("\nAn assassin strikes from the shadows!")
    damage = random.randint(3,5)
    character["hp"] -= damage
    type_text_slowly(f"You lose {damage} HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def sacrifice_challenge(character):
    type_text_slowly("\nA shrine demands sacrifice.")
    print("[1] Offer blood")
    print("[2] Refuse")
    choice = input("Your choice: ").strip()
    while choice not in ["1","2"]:
        choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        character["hp"] -= 2
        character["experience"] += 2
        character["honor"] -= 2
        character["bond_with_Ryūichi"] -= 1
        type_text_slowly("Power answers your blood. Ryūichi turns away in silence.")
        print(f"HP: {character['hp']}/{character['max_hp']}")
        print(f"Experience: {character['experience']}")
    else:
        character["honor"] += 2
        character["bond_with_Ryūichi"] += 1
        type_text_slowly("You refuse the dark power. Ryūichi nods with respect.")

def final_boss_fight(character):
    if character["path"] == "ronin":
        boss = "the Emperor"
        type_text_slowly("\nYou storm the palace with Ryūichi at your side.")
    else:
        boss = character["friend_name"]
        type_text_slowly(f"\nRyūichi stands before you as a hardened Ronin.")

    boss_hp = 20 + (character["level"] * 5)

    while boss_hp > 0 and character["hp"] > 0:
        print(f"\nYour HP: {character['hp']}/{character['max_hp']} | {boss} HP: {boss_hp}")
        print("[1] Attack")
        print("[2] Defend")
        print("[3] Risky Strike\n")

        choice = input("Your move: ").strip()
        while choice not in ["1", "2", "3"]:
            choice = input("Invalid choice. Enter 1, 2, or 3: ").strip()

        player_roll = random.randint(1, 10) + character["attack_power"]
        boss_roll = random.randint(1, 10) + 4

        if choice == "1":
            if player_roll >= boss_roll:
                damage = 4 + (character["level"] * 2)
                boss_hp -= damage
                type_text_slowly(f"You strike for {damage} damage. {boss} HP: {boss_hp}")
            else:
                damage = 4 + character["level"]
                character["hp"] -= damage
                type_text_slowly(f"You are struck for {damage} damage.")
                print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "2":
            reduced = 1 + character["level"]
            character["hp"] -= reduced
            type_text_slowly(f"You block but take {reduced} damage.")
            print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "3":
            if random.randint(1, 10) >= 6:
                damage = 7 + (character["level"] * 3)
                boss_hp -= damage
                type_text_slowly(f"Your all-out strike deals {damage} damage. {boss} HP: {boss_hp}")
            else:
                character["hp"] -= 5
                type_text_slowly("Your all-out strike fails. You take 5 damage.")
                print(f"HP: {character['hp']}/{character['max_hp']}")

    if character["hp"] > 0:
        type_text_slowly(f"\nYou have defeated {boss}.")
        return True

    character["hp"] = 0
    print(f"HP: {character['hp']}/{character['max_hp']}")
    return False

def main():
    test_character = {
        "hp": 10,
        "max_hp": 10,
        "attack_power": 5,
        "experience": 2
    }


    sacrifice_challenge(test_character)


if __name__ == "__main__":
    main()

