import random
import time
import sys

def ryuichi_present(character):
    return character["path"] == "ronin"

def type_text_slowly(text, delay=0.04):
    for character in str(text):
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def execute_challenge(character):
    interactive_challenge = [
        "combat", "riddle", "moral", "traveler",
        "duel", "sacrifice", "gamble",
        "hostage", "wounded_soldier",
        "execution", "duel_of_honor",
        "burning_village"
    ]
    passive_challenge = [
        "ambush", "storm", "merchant", "healer",
        "spirit", "feast", "thief",
        "boar_charge", "bridge", "fire",
        "blessing", "training",
        "pilgrim", "assassin", "shrine"
    ]

    if random.randint(1, 10) <= 7:
        challenge_type = random.choice(interactive_challenge)
    else:
        challenge_type = random.choice(passive_challenge)

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
    elif challenge_type == "spirit":
        spirit_challenge(character)
    elif challenge_type == "feast":
        feast_challenge(character)
    elif challenge_type == "thief":
        thief_challenge(character)
    elif challenge_type == "boar_charge":
        boar_charge_challenge(character)
    elif challenge_type == "bridge":
        bridge_challenge(character)
    elif challenge_type == "fire":
        fire_challenge(character)
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
                type_text_slowly(f"\nYou strike the {enemy} for 3 damage!")
            else:
                character["hp"] -= 3
                type_text_slowly(f"\nThe {enemy} hits you for 3 damage!")
                print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "2":
            character["hp"] -= 1
            type_text_slowly("\nYou defend but still take 1 damage.")
            print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "3":
            if random.randint(1, 10) >= 4:
                type_text_slowly(f"\nYou are being watched by the locals and can't run! The {enemy} strikes you!")
                character["hp"] -= 1
            else:
                type_text_slowly("\nYou cover your face and flee!")
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
    type_text_slowly("\nYou discover a glowing shrine.")
    print("[1] Drink from the shrine")
    print("[2] Leave it alone")

    choice = input("Your choice: ").strip()
    while choice not in ["1", "2"]:
        choice = input("Invalid choice. Enter 1 or 2: ").strip()

    if choice == "1":
        heal = random.randint(1, 3)
        if character["hp"] == character["max_hp"]:
            type_text_slowly("\nThis shrine's water tastes like moldy feet and old coins.")
        else:
            character["hp"] = min(character["hp"] + heal, character["max_hp"])
            type_text_slowly(f"\nYou feel warmth. HP restored by {heal}.")
            print(f"HP: {character['hp']}/{character['max_hp']}")
    else:
        print("\nYou bow and walk away.")

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
        if ryuichi_present(character):
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
            type_text_slowly(f"\"We will find dinner elsewhere don't worry {character["name"]}\"")
        else:
            type_text_slowly("\nYou give your last food away to the thief and walk on in silence.")
    print(f"Experience: {character['experience']}")

def ambush_challenge(character):
    type_text_slowly("\nBandits leap from the trees!")
    damage = random.randint(2,4)
    character["hp"] -= damage
    type_text_slowly(f"\nYou escape but lose {damage} HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def traveler_challenge(character):
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
            type_text_slowly("Y\nou leave the traveler behind without looking back.")

def gamble_challenge(character):
    type_text_slowly("\nA dice gambler challenges you.")
    roll = random.randint(1,10)
    if roll >= 6:
        character["experience"] += 1
        type_text_slowly("\nYou win the gamble. You gain 1 experience.")
    else:
        character["hp"] -= 2
        type_text_slowly("\nYou lose and take 2 HP damage.")
        print(f"HP: {character['hp']}/{character['max_hp']}")

def storm_challenge(character):
    type_text_slowly("\nA violent storm batters you.")
    character["hp"] -= 1
    type_text_slowly("\nYou lose 1 HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def merchant_challenge(character):
    type_text_slowly("\nA merchant overcharges you for supplies.")
    character["hp"] += 1 if character["hp"] < character["max_hp"] else 0
    type_text_slowly("\nYou recover 1 HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def healer_challenge(character):
    type_text_slowly("\nA wandering healer treats your wounds.")
    heal = 2
    character["hp"] = min(character["hp"] + heal, character["max_hp"])
    type_text_slowly(f"\nYou gain {heal} HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def spirit_challenge(character):
    type_text_slowly("\nA spirit blocks your path.")
    if character["honor"] >= 3:
        character["experience"] += 2
        type_text_slowly("\nThe spirit bows and grants you power. You gain 2 experience.")
    elif character["honor"] <= -2:
        character["hp"] -= 2
        type_text_slowly("\nThe spirit recoils from your darkness. You lose 2 HP.")
    else:
        type_text_slowly("\nThe spirit watches silently and vanishes.")

def feast_challenge(character):
    type_text_slowly("\nA village offers you a feast.")
    character["hp"] = min(character["hp"] + 3, character["max_hp"])
    type_text_slowly("\nYou recover 3 HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def thief_challenge(character):
    type_text_slowly("\nA thief steals from you in the night.")
    character["experience"] -= 1
    type_text_slowly("\nYou lose 1 experience.")
    print(f"Experience: {character['experience']}")

def boar_charge_challenge(character):
    type_text_slowly("\nA wild boar charges!")
    damage = random.randint(2,4)
    character["hp"] -= damage
    type_text_slowly(f"\nYou take {damage} HP damage.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def bridge_challenge(character):
    type_text_slowly("\nA broken bridge blocks your path.")
    if random.randint(1,10) >= 5:
        type_text_slowly("\nYou cross safely.")
    else:
        character["hp"] -= 2
        type_text_slowly("\nYou fall and lose 2 HP.")
        print(f"HP: {character['hp']}/{character['max_hp']}")

def fire_challenge(character):
    type_text_slowly("\nA sudden fire engulfs the path.")
    character["hp"] -= 3
    type_text_slowly("\nYou lose 3 HP.")
    print(f"HP: {character['hp']}/{character['max_hp']}")

def blessing_challenge(character):
    type_text_slowly("\nA monk blesses your journey.")
    character["experience"] += 1
    type_text_slowly("\nYou gain 1 experience.")
    print(f"Experience: {character['experience']}")


def training_challenge(character):
    type_text_slowly("\nA veteran trains you briefly.")
    character["experience"] += 2
    type_text_slowly("\nYou gain 2 experience.")
    print(f"Experience: {character['experience']}")

def pilgrim_challenge(character):
    type_text_slowly("\nA pilgrim shares wisdom.")
    character["experience"] += 1
    type_text_slowly("\nYou gain 1 experience.")
    print(f"Experience: {character['experience']}")

def assassin_challenge(character):
    type_text_slowly("\nAn assassin strikes from the shadows!")
    damage = random.randint(3,5)
    character["hp"] -= damage
    type_text_slowly(f"\nYou lose {damage} HP.")
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
        character["attack_power"] += 2
        character["experience"] += 2
        character["honor"] -= 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 1
            type_text_slowly("\nPower answers your blood. You lose 2 HP but gain 2 attack. Ryūichi turns away in silence.")
        else:
            type_text_slowly("\nDark power floods your veins. You lose 2 HP but gain 2 attack.")
        print(f"HP: {character['hp']}/{character['max_hp']} | Experience: {character['experience']}")
        print(f"Attack power: {character['attack_power']}")
    else:
        character["honor"] += 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] += 1
            type_text_slowly("\nYou refuse the dark power. Ryūichi nods with respect.")
        else:
            type_text_slowly("\nYou resist the temptation and walk on.")


def hostage_challenge(character):
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
                character["experience"] += 1
                type_text_slowly("\nYou strike fast and save the hostage.")
        else:
            if ryuichi_present(character):
                character["bond_with_Ryūichi"] += 1
                type_text_slowly("\nYou attempt to save the villager but you do not make it in time.")
                type_text_slowly("You viciously kill the bandits in a fit of rage.")
                type_text_slowly("Ryūichi rubs your back and consoles you.")
            else:
                character["experience"] += 1
                type_text_slowly("\nYou attempt to save the villager but you do not make it in time.")
                type_text_slowly("You viciously kill the bandits in a fit of rage.")
        print(f"Experience: {character['experience']}")
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
        print(f"Experience: {character['experience']}")
    else:
        character["honor"] -= 2
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 1
            type_text_slowly("\nYou decide to leave them to their fate.")
            type_text_slowly("Ryūichi looks at you in frustration and steps in to save the villager")
        else:
            type_text_slowly("\nYou decide to leave them to their fate.")

def wounded_soldier_challenge(character):
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
        character["honor"] -= 2
        if ryuichi_present(character):
            type_text_slowly("\nYou kill the wounded soldier. Ryūichi turns away, shaken.")
        else:
            type_text_slowly("\nYou grant him a quick death.")
    else:
        character["honor"] -= 1
        type_text_slowly("\nYou leave him behind to suffer.")

def execution_challenge(character):
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
        type_text_slowly("\nYou say nothing as the blade falls.")
    else:
        character["honor"] -= 3
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 2
            type_text_slowly("\nYou gleefully help the executioner. Ryūichi looks at you in disbelief.")
        else:
            type_text_slowly("\nYou coldly assist the execution without question.")

def duel_of_honor_challenge(character):
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
        print(f"Experience: {character['experience']}")
    elif choice == "2":
        if ryuichi_present(character):
            type_text_slowly("\nYou shove dirt in the warriors face then stab him in the groin.")
            type_text_slowly("Ryūichi hangs his head in shame.")
        else:
            character["experience"] += 1
            character["honor"] -= 2
            type_text_slowly("\nYou shove dirt in the warriors face then stab him in the groin.")
        print(f"Experience: {character['experience']}")
    else:
        character["honor"] -= 1
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 1
            type_text_slowly("\nYou walk away as the crowd jeers. Ryūichi looks at you in disappointment.")
        else:
            type_text_slowly("\nYou walk away as the crowd jeers.")

def burning_village_challenge(character):
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
        else:
            type_text_slowly("\nAs the village burns, you cut down fleeing attackers through smoke and fire.")
    else:
        if ryuichi_present(character):
            character["bond_with_Ryūichi"] -= 2
            character["honor"] -= 2
            type_text_slowly("\nRyūichi shoves you to the ground as you try and steal from the burning village.")
        else:
            character["honor"] -= 2
            character["experience"] += 1
            type_text_slowly("\nYou scavenge what supplies you can from the burning ruins and move on.")
    print(f"Experience: {character['experience']}")

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
        "experience": 2,
        "name": "jameel",
        "path": "ronin",
        "friend_name": "Ryūichi",
        "x-coordinate": 0,
        "y-coordinate": 0,
        "level": 1,
        "bond_with_Ryūichi": 0,
        "honor": 0,
        "betrayal": False
    }
    burning_village_challenge(test_character)


if __name__ == "__main__":
    main()

