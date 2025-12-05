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




def print_death_screen(character):
    banner = pyfiglet.figlet_format("YOU HAVE FALLEN", font="doom")
    print(banner)
    type_text_slowly(f"{character['name']}'s blade falls into the dust.")
    type_text_slowly("The wind carries your story into silence...\n")


def print_victory_screen(character):
    banner = pyfiglet.figlet_format("VICTORY", font="big")
    print(banner)

    if character["betrayal"]:
        type_text_slowly("Ryūichi lies motionless in the dust.")
        type_text_slowly("His eyes never forgave you.")
        type_text_slowly("Victory tastes like ash in your mouth.\n")
    elif character["bond_with_Ryūichi"] >= 4:
        if character["path"] == "ronin":
            type_text_slowly("The Emperor lies defeated.")
            type_text_slowly("Ryūichi grips your arm tightly as the palace burns.")
            type_text_slowly("Two brothers standing at the end of an empire.\n")
        else:
            type_text_slowly("Ryūichi kneels before you, wounded but alive.")
            type_text_slowly("\"We survived,\" he whispers. \"That is enough.\"\n")
    else:
        if character["path"] == "ronin":
            type_text_slowly("The Emperor lies defeated.")
            type_text_slowly("Ryūichi disappears into the smoke without a word.")
            type_text_slowly("Some victories are won alone.\n")
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

def final_duel_intro(character):
    if character["betrayal"]:
        type_text_slowly("\nRyūichi steps forward with cold eyes.")
        type_text_slowly("\"You chose chaos over brotherhood.\"")
    elif character["path"] == "ronin":
        type_text_slowly("\nRyūichi stands beside you at the gates of the palace.")
        type_text_slowly("\"We finish this together...or not at all.\"")
    else:
        type_text_slowly("\nRyūichi blocks your path.")
        type_text_slowly("\"You wear the Emperor’s chains now.\"")

def choose_path():
    type_text_slowly("\nThe rain falls softly on the village of your childhood.")
    type_text_slowly("You stand beneath the eaves of a ruined shrine, armor wet, blade heavy at your side.")
    type_text_slowly("Beside you stands Ryūichi — your brother in battle since youth.\n")

    type_text_slowly("Together, you trained under the same master.")
    type_text_slowly("Together, you survived your first war.")
    type_text_slowly("And together, you now stand at the edge of a divided future.\n")

    type_text_slowly("Ryūichi turns to you, rain tracing lines down his hardened face.")
    type_text_slowly("\"The Emperor tightens his grip on the land,\" he says quietly.")
    type_text_slowly("\"Order is coming... whether through law — or blood.\"")
    type_text_slowly("\"Tonight, we choose who we become.\"\n")

    type_text_slowly("He steps closer and holds his hand out.")
    type_text_slowly("\"Stand with me,\" he says.")
    type_text_slowly("\"Not as soldiers. Not as weapons.\"")
    type_text_slowly("\"But as brothers.\"\n")

    while True:
        type_text_slowly("Choose your path:\n")

        print("[1] Samurai — Swear loyalty to the Emperor")
        type_text_slowly("    You will wear the symbol of the throne.")
        type_text_slowly("    You will fight for law, order, and the stability of the realm.")
        type_text_slowly("    Even if that means standing against your own past.\n")

        print("[2] Ronin — Walk the shadowed road with Ryūichi")
        type_text_slowly("    You will become an enemy of the state.")
        type_text_slowly("    You will strike from the dark to tear down a broken empire.")
        type_text_slowly("    Even if it costs you everything.\n")

        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            type_text_slowly("\nYou lower your head.")
            type_text_slowly("\"The throne must be protected,\" you say.")
            type_text_slowly("\"Even from itself.\"")
            type_text_slowly("\nRyūichi exhales slowly.")
            type_text_slowly("\"Then this is where our paths split, my friend.\"")
            type_text_slowly("\"May your blade never waver.\"\n")
            return "samurai"

        if choice == "2":
            type_text_slowly("\nYou tighten your grip on your blade.")
            type_text_slowly("\"The Empire is rotting,\" you whisper.")
            type_text_slowly("\"And I will not die defending a lie.\"")
            type_text_slowly("\nRyūichi smiles for the first time in years.")
            type_text_slowly("\"Then we walk as ghosts,\" he says.")
            type_text_slowly("\"And we reshape history with steel.\"\n")
            return "ronin"
