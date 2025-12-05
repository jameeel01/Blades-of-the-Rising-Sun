import pyfiglet
import time
import sys

def type_text_slowly(text, delay=0.02):
    for character in str(text):
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


def print_title_screen():
    result = pyfiglet.figlet_format("BLADES OF THE RISING SUN", font="doom")
    print(result)

def print_intro_story(character):
    if character["path"] == "samurai":
        type_text_slowly(
            "You chose the path of the Samurai — to serve the Emperor and bring order from within."
        )
        type_text_slowly("Ryūichi turned away from the throne.\n")
    else:
        type_text_slowly(
            "You chose the lonely road of the Ronin — to fight the throne from the shadows."
        )
        type_text_slowly("Ryūichi remained loyal to the Emperor.\n")

    type_text_slowly(
        f"As children, {character['name']} and Ryūichi trained together under a fallen master."
    )
    type_text_slowly("They swore an oath beneath the cherry blossoms to protect one another.\n")

    type_text_slowly("Now your journey begins...\n")


def print_death_screen(character):
    banner = pyfiglet.figlet_format("YOU HAVE FALLEN", font="doom")
    print(banner)
    type_text_slowly(f"{character['name']}'s blade falls into the dust.")
    type_text_slowly("The wind carries your story into silence...\n")


def print_victory_screen(character):
    banner = pyfiglet.figlet_format("VICTORY", font="big")
    print(banner)

    if character["path"] == "ronin":
        type_text_slowly("The Emperor lies defeated.")
        type_text_slowly("Ryūichi collapses beside you, smiling at last.")
        type_text_slowly("Peace comes at the cost of blood.\n")
    else:
        type_text_slowly("Ryūichi falls at your feet.")
        type_text_slowly("The Emperor declares the land stable.")
        type_text_slowly("But your heart feels heavy with loss.\n")

    type_text_slowly(f"{character['name']} stands beneath the rising sun.")
    type_text_slowly("Your legend is written in steel and sacrifice.\n")


def print_final_duel_banner(boss_name):
    banner = pyfiglet.figlet_format("FINAL DUEL", font="slant")
    print(banner)
    print(f"You face {boss_name}.\n")

def choose_path():
    while True:
        print("Choose your path:\n")
        print("[1] Samurai:")
        type_text_slowly("    Serve the Emperor with honor and law.")
        type_text_slowly("    You fight for order, tradition, and the stability of the realm.\n")
        print("[2] Ronin:")
        type_text_slowly("    A masterless warrior betrayed by the throne.")
        type_text_slowly("    You fight from the shadows to tear down the corrupt empire.\n")

        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            return "samurai"
        if choice == "2":
            return "ronin"
