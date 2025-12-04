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
    else:
        moral_challenge(character)

def combat_challenge(character):
    foes = ["lost child", "rogue samurai", "wild boar", "mountain thief", "seductive ninja"]
    enemy = random.choice(foes)
    enemy_hp = 6

    print(f"\nA {enemy} challenges you to battle!")

    while enemy_hp > 0 and character["hp"] > 0:
        print(f"\nYour HP: {character['hp']}/{character['max_hp']} | {enemy.title()} HP: {enemy_hp}")
        print("[1] Attack")
        print("[2] Defend")
        print("[3] Run away")

        choice = input("Your move: ").strip()
        while choice not in ["1", "2", "3"]:
            choice = input("Invalid choice. Enter 1, 2, or 3: ").strip()

        player_roll = random.randint(1, 10) + character["attack_power"]
        enemy_roll = random.randint(1, 10)

        if choice == "1":
            if player_roll >= enemy_roll:
                enemy_hp -= 3
                print(f"You strike the {enemy} for 3 damage!")
            else:
                character["hp"] -= 3
                print(f"The {enemy} hits you for 3 damage!")
                print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "2":
            character["hp"] -= 1
            print("You defend but still take 1 damage.")
            print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "3":
            if random.randint(1, 10) >= 4:
                print("You are being watched by the locals and can't run!")
            else:
                print("You cover your face and flee!")
                break

    if enemy_hp <= 0:
        print(f"\nYou have defeated the {enemy}.")
        character["experience"] += 1
        print(f"Experience increased to {character['experience']}")
    else:
        print("\nYou retreat from battle.")

def riddle_challenge(character):
    print("\nA wandering monk stops you.")
    print("What walks on four legs in the morning, two at noon, and three in the evening?")
    print("[1] A dragon")
    print("[2] A human")
    print("[3] A wolf")
    print("[4] A mouse")

    answer = input("Your choice: ").strip()
    while answer not in ["1", "2", "3", "4"]:
        answer = input("Invalid choice. Enter 1, 2, 3, or 4: ").strip()

    if answer == "2":
        character["experience"] += 1
        print("Correct. You gain 1 experience.")
        print(f"Experience: {character['experience']}")
    else:
        character["hp"] -= 2
        print("The monk stabs you for insulting his intelligence. You lose 2 HP.")
        print(f"HP: {character['hp']}/{character['max_hp']}")

def shrine_challenge(character):
    print("\nYou discover a glowing shrine.")
    print("[1] Drink from the shrine")
    print("[2] Leave it alone")

    choice = input("Your choice: ").strip()
    while choice not in ["1", "2"]:
        choice = input("Invalid choice. Enter 1 or 2: ").strip()

    if choice == "1":
        heal = random.randint(1, 3)
        if character["hp"] == character["max_hp"]:
            print("This shrine's water tastes like moldy feet and old coins.")
        else:
            character["hp"] = min(character["hp"] + heal, character["max_hp"])
            print(f"You feel warmth. HP restored by {heal}.")
            print(f"HP: {character['hp']}/{character['max_hp']}")
    else:
        print("You bow and walk away.")

def moral_challenge(character):
    print("\nA starving thief steals rice from a farmer.")
    print("[1] Kill the thief")
    print("[2] Let the thief go")
    print("[3] Give your own food")

    choice = input("Your choice: ").strip()
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Enter 1, 2, or 3: ").strip()

    if choice == "1":
        character["experience"] += 1
        print("You kill the thief. You gain 1 experience.")
        print(f"Experience: {character['experience']}")
    elif choice == "2":
        character["experience"] -= 1
        print("The thief escapes. The farmer curses your name. You lose 1 experience")
        print(f"Experience: {character['experience']}")
    elif choice == "3":
        character["hp"] -= 2
        print("You give your food and starve for the rest of the day. You lose 2 HP.")
        print(f"HP: {character['hp']}/{character['max_hp']}")

def final_boss_fight(character):
    if character["path"] == "ronin":
        boss = "the Emperor"
        print("\nYou storm the palace with Ryūichi at your side.")
    else:
        boss = character["friend_name"]
        print(f"\nRyūichi stands before you as a hardened Ronin.")

    boss_hp = 20

    while boss_hp > 0 and character["hp"] > 0:
        print(f"\nYour HP: {character['hp']}/{character['max_hp']} | {boss} HP: {boss_hp}")
        print("[1] Attack")
        print("[2] Defend")
        print("[3] Risky Strike")

        choice = input("Your move: ").strip()
        while choice not in ["1", "2", "3"]:
            choice = input("Invalid choice. Enter 1, 2, or 3: ").strip()

        player_roll = random.randint(1, 10) + character["attack_power"]
        boss_roll = random.randint(1, 10) + 4

        if choice == "1":
            if player_roll >= boss_roll:
                boss_hp -= 4
                print(f"You strike for 4 damage. {boss} HP: {boss_hp}")
            else:
                character["hp"] -= 4
                print(f"You are struck for 4 damage.")
                print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "2":
            reduced = random.randint(1, 3)
            character["hp"] -= reduced
            print(f"You block but take {reduced} damage.")
            print(f"HP: {character['hp']}/{character['max_hp']}")

        elif choice == "3":
            if random.randint(1, 10) >= 6:
                boss_hp -= 7
                print(f"Your all-out strike deals 7 damage. {boss} HP: {boss_hp}")
            else:
                character["hp"] -= 5
                print("Your all-out strike fails. You take 5 damage.")
                print(f"HP: {character['hp']}/{character['max_hp']}")

    if character["hp"] > 0:
        print(f"\nYou have defeated {boss}.")
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


    moral_challenge(test_character)


if __name__ == "__main__":
    main()

