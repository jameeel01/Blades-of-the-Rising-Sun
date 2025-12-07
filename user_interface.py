"""
Jameel Mohammed
A01430376
No unit tests were done for this module as it consists of print statements and ASCII
"""
import pyfiglet
import time
import sys
import random

def type_text_slowly(text, delay=0.03):
    """
    Print text to the screen one character at a time with a delay.

    :param text: a string of text
    :param delay: a float representing delay between each character
    :precondition: text must be convertible to a string
    :postcondition: text is delayed when displayed to the terminal
    :return: text output printed letter by letter
    """
    for character in str(text):
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def print_title_screen():
    """
    Display the game title in large ASCII art format.

    :precondition: pyfiglet library must be installed
    :postcondition: the game title banner is printed to the terminal
    :return: generated ASCII banner as a string
    """
    result = pyfiglet.figlet_format("BLADES OF THE RISING SUN", font="doom")
    print(result)

def print_intro_story(character):
    """
    Display the introductory story based on the player's chosen path.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains a valid "path" key
    :postcondition: the appropriate story text is displayed
    :return: displayed story text as a string
    """
    if character["path"] == "samurai":
        type_text_slowly(
            "You chose the path of the Samurai — to serve the Emperor and bring order from within."
        )
        type_text_slowly("Ryūichi turned away from the throne.\n")
    else:
        type_text_slowly(
            "You chose the lonely road of the Ronin — to fight the throne from the shadows."
        )
        type_text_slowly("You join arms with Ryūichi to take down the Emperor.\n")

def explain_game_goal(character):
    """
    Explain the main objective of the game based on the player's path.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains a valid "path" key
    :postcondition: the game objective is printed to the terminal
    :return: printed objective text as a string
    """
    type_text_slowly("\nThe Empire stands on the edge of collapse.")
    type_text_slowly("Rebels rise in the shadows. The Emperor (帝) clings to power.\n")

    if character["path"] == "ronin":
        type_text_slowly("You (人) walk the road to the palace to kill the Emperor (帝).")
        type_text_slowly("Your blade will decide the fate of the Empire.\n")
    else:
        type_text_slowly("You (人) march toward the palace to protect the Emperor (帝).")
        type_text_slowly("You will stand against the rising ronins.\n")

    type_text_slowly("Grow strong enough to reach the final battlefield.")
    type_text_slowly("Choose who you become.")
    type_text_slowly("Survive the last duel beneath the rising sun.\n")

def choose_path():
    """
    Prompt the user to choose between the Samurai and Ronin paths.

    User has the option to skip the intro or tutorial.

    :precondition: user must enter valid inputs
    :postcondition: the selected path is returned as a string
    :return: "samurai" or "ronin"
    """
    while True:
        skip_intro = input("Skip intro? (Y/N): ").strip().lower()
        if skip_intro in ["y", "n"]:
            break
        print("Invalid input. Please enter Y or N.")

    if skip_intro != "y":
        type_text_slowly("\nThe rain falls softly on the village of your childhood.")
        type_text_slowly("You stand beneath the eaves of a ruined shrine. You remember fond memories of your time spent in the village.")
        type_text_slowly("Beside you stands Ryūichi — your brother in battle since youth.\n")

        type_text_slowly("Together, you trained under the same master and survived your first war.")
        type_text_slowly("Together as samurai, you stand in pain gazing at the village you grew up in.\n")
        type_text_slowly("Ryūichi turns to you, rain tracing lines down his hardened face.")
        type_text_slowly("\"The Emperor tightens his grip on the land,\" he says quietly.")
        type_text_slowly("\"Order is coming... whether through law — or blood.\"")
        type_text_slowly("\"Tonight, we choose who we become.\"\n")

        type_text_slowly("You look into his eyes and see no traces of the friend you grew up with.")
        type_text_slowly("There is only a product of war.\n")

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
            if skip_intro != "y":
                type_text_slowly("\nYou lower your head.")
                type_text_slowly("\"The throne must be protected,\" you say.")
                type_text_slowly("\"Even from itself.\"")
                type_text_slowly("\nRyūichi exhales slowly.")
                type_text_slowly("\"Then this is where our paths split, my friend.\"")
                type_text_slowly("\"I no longer wish to fight for this Empire\"")
                type_text_slowly("\"May your blade never waver.\"\n")
            return "samurai"

        elif choice == "2":
            if skip_intro != "y":
                type_text_slowly("\nYou tighten your grip on your blade.")
                type_text_slowly("\"The Empire is rotting,\" you whisper.")
                type_text_slowly("\"And I will not die defending a lie.\"")
                type_text_slowly("\nRyūichi smiles for the first time in years.")
                type_text_slowly("\"Then we walk as ghosts,\" he says.")
                type_text_slowly("\"And we reshape history with steel.\"\n")
            return "ronin"

        else:
            print("Invalid choice. Please enter 1 or 2.")

def print_death_screen(character):
    """
    Display the game-over screen when the player dies.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains a valid "name"
    :postcondition: the death banner and story text are printed
    :return: printed death message as a string
    """
    banner = pyfiglet.figlet_format("YOU HAVE DIED", font="doom")
    print(banner)
    type_text_slowly(f"\n{character['name']}'s blade falls into the dust.")
    type_text_slowly("The wind carries your story into silence...\n")

def print_victory_screen(character):
    """
    Display the victory ending based on the player's final decisions.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains "path", "betrayal", and "bond_with_Ryūichi"
    :postcondition: the correct ending text is printed to the terminal
    :return: printed victory story as a string
    """
    if character["betrayal"]:
        type_text_slowly("Ryūichi lies motionless in the dust.")
        type_text_slowly("His eyes never forgave you.")
        type_text_slowly("Victory tastes like ash in your mouth.\n")
    elif character["bond_with_Ryūichi"] >= 4:
        if character["path"] == "ronin":
            type_text_slowly("Ryūichi grips your arm tightly as the palace burns.")
            type_text_slowly("Two brothers standing at the end of an empire.\n")
        else:
            type_text_slowly("Ryūichi kneels before you, wounded but alive.")
            type_text_slowly("\"We survived,\" he whispers. \"That is enough.\"\n")
    else:
        if character["path"] == "ronin":
            type_text_slowly("Ryūichi disappears into the smoke without a word.")
            type_text_slowly("Some victories are won alone.\n")
        else:
            type_text_slowly("Ryūichi falls at your feet.")
            type_text_slowly("The Emperor declares the land stable.")
            type_text_slowly("But your heart feels heavy with loss.\n")

    type_text_slowly(f"{character['name']} stands beneath the rising sun.")
    type_text_slowly("Your legend is written in steel and sacrifice.\n")

    banner = pyfiglet.figlet_format("VICTORY", font="big")
    print(banner)

def print_final_duel_banner():
    """
    Display the final duel title banner in ASCII art.

    :precondition: pyfiglet library is installed
    :postcondition: the banner is printed to the terminal
    :return: the generated ASCII banner as a string
    """
    banner = pyfiglet.figlet_format("\nFINAL DUEL", font="slant")
    print(banner)

def final_duel_intro(character):
    """
    Display opening dialogue for the final duel based on character state.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains "path" and "betrayal"
    :postcondition: the appropriate duel intro dialogue is printed
    :return: the displayed duel dialogue as a string
    """
    if character["betrayal"]:
        type_text_slowly("\nRyūichi steps forward with cold eyes.")
        type_text_slowly("\"You chose chaos over brotherhood.\"")
    elif character["path"] == "ronin":
        type_text_slowly("\nRyūichi stands beside you at the gates of the palace.")
        type_text_slowly("\"We finish this together...or not at all.\"")
    else:
        type_text_slowly("\nRyūichi blocks your path.")
        type_text_slowly("\"You wear the Emperor’s chains now.\"")


def ryuichi_random_dialogue(character):
    """
    Display a random line of dialogue from Ryūichi based on the player's honor.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains "honor" and "path"
    :postcondition: one randomized dialogue line may be printed
    :return: the selected dialogue line as a string
    """
    if character["path"] == "samurai":
        return

    tragic_lines = [
        "\"We were boys when we learned to kill...was there ever another way?\"",
        "\"Every road we walk seems soaked in blood now.\""
    ]

    vengeful_lines = [
        "\"The Emperor will choke on his gold.\"",
        "\"Mercy built this rotten empire.\""
    ]

    honor_lines = [
        "\"A blade must serve purpose, or it becomes a curse.\"",
        "\"Even rebels must have rules.\""
    ]

    if character["honor"] >= 3:
        line = random.choice(honor_lines)
    elif character["honor"] <= -3:
        line = random.choice(vengeful_lines)
    else:
        line = random.choice(tragic_lines)

    type_text_slowly(f"\nRyūichi: {line}\n")

def ryuichi_flashback(character):
    """
    Display a flashback memory based on the player's bond with Ryūichi.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains "bond_with_Ryūichi"
    :postcondition: one randomized memory scene is printed
    :return: the displayed flashback text as a string
    """
    if character["bond_with_Ryūichi"] >= 4:
        flashbacks = [
            "You remember the two of you stealing training swords as children.\n",
            "You remember Ryūichi shielding you from your master's strike.\n",
            "You remember laughing beside the fire after your first victory together.\n"
        ]
    elif character["bond_with_Ryūichi"] <= -2:
        flashbacks = [
            "You remember the night Ryūichi turned his back on you.\n",
            "You remember the argument that ended in drawn blades.\n",
            "You remember walking away while he stood alone in the rain.\n"
        ]
    else:
        flashbacks = [
            "You remember training with Ryūichi from dawn to dusk.\n",
            "You remember fighting side by side with Ryūichi during the war.\n",
            "You remember Ryūichi dragging you from the battlefield while bleeding.\n"
        ]

    type_text_slowly("\n[FLASHBACK]: ")
    type_text_slowly(random.choice(flashbacks))

def determine_betrayal(character):
    """
    Determine whether Ryūichi betrays the player based on bond and honor.

    :param character: a dictionary representing the player's character
    :precondition: character dictionary contains "path", "bond_with_Ryūichi", and "honor"
    :postcondition: character "betrayal" or "honor" changes based on choice
    :return: the updated character dictionary
    """
    if character["path"] == "samurai":
        character["betrayal"] = False
        return
    if character["bond_with_Ryūichi"] <= -2 or character["honor"] <= -4:
        character["betrayal"] = True
    else:
        character["betrayal"] = False



def final_boss_intro_samurai():
    """
    Display the final boss introduction for the Samurai path.

    :precondition: character is level 3 and at location (9, 9)
    :precondition: character dictionary "path" is samurai
    :postcondition: the Samurai final boss intro narrative is printed
    :return: the printed Samurai boss intro story as a string
    """
    type_text_slowly("\nThe wind dies as you step into the Emperor's palace.")
    type_text_slowly("Ash drifts slowly through the air like falling snow.")
    type_text_slowly("You bow and greet the Emperor.\n")

    type_text_slowly("The Emperor studies you with tired, calculating eyes.")
    type_text_slowly("\"The head of the Ronin has eluded my armies for months,\" he says.")
    type_text_slowly("\"End this rebellion. Bring me his head.\"")
    type_text_slowly("You feel the weight of the command settle into your chest.\n")

    type_text_slowly("\"Your Majesty I—")
    print("The palace doors explode inward with the scream of splintering wood.\n")

    type_text_slowly("You can't believe your eyes.")
    type_text_slowly("Ryūichi stands before you as the Leader of Ronins.")
    type_text_slowly("His armor is cracked. His blade is stained dark.\n")

    type_text_slowly("\"So this is where our blades finally meet,\" he says quietly.")
    type_text_slowly("\"We are enemies forged by the same war.\"\n")

    type_text_slowly("You raise your weapon.")
    type_text_slowly("Your hands do not tremble — but your heart does.\n")

    type_text_slowly("\"I never wanted this,\" Ryūichi says.")
    type_text_slowly("\"But destiny has never cared for what we want.\"\n")


def final_boss_outro_samurai():
    """
    Display the concluding narration after Samurai character defeats Ryūichi in the final duel.

    :precondition: character dictionary "path" is samurai
    :precondition: character has defeated Ryūichi
    :postcondition: Ryūichi’s defeat scene is printed to the terminal
    :return: the displayed outro narration as a string
    """
    type_text_slowly("\nRyūichi staggers back, dropping to one knee.")
    type_text_slowly("His blade slips from his fingers and clatters across the stone.\n")

    type_text_slowly("He looks up at you one last time.")
    type_text_slowly("\"Finish it,\" he whispers.")
    type_text_slowly("\"Let the world remember only one of us.\"\n")

def final_boss_intro_ronin():
    """
    Display the opening narration for the Ronin entering the Emperor’s palace.

    :precondition: character has chosen the Ronin path and reached the final area
    :precondition: character is level 3 and at location (9, 9)
    :postcondition: the final boss intro narrative is printed
    :return: the displayed Ronin boss intro as a string
    """
    type_text_slowly("\nYou storm the palace with Ryūichi at your side.")
    type_text_slowly("The great wooden gates burst open under your combined force.")

    type_text_slowly("Imperial guards fall back in terror as you advance.")
    type_text_slowly("Your blades are slick with blood, your breath heavy with smoke.\n")

    type_text_slowly("Ahead, the towering doors of the throne room tremble.")
    type_text_slowly("With a final strike, they collapse inward.\n")

    type_text_slowly("The Emperor stands alone upon his throne.")
    type_text_slowly("Golden armor gleams beneath the firelight, unshaken.")
    type_text_slowly("He regards you not with fear — but with cold certainty.\n")

    type_text_slowly("\"So,\" the Emperor says, rising slowly.")
    type_text_slowly("\"The ghosts of my empire have come at last.\"")

    type_text_slowly("Ryūichi steps forward beside you.")
    type_text_slowly("\"Your reign ends here,\" he says.\n")

def emperor_death_scene():
    """
    Display the death scene of the Emperor after being defeated in combat.

    :precondition: character has chosen the Ronin path
    :precondition: the Emperor has been defeated in the final battle
    :postcondition: the Emperor’s death narration is printed to the terminal
    :return: the displayed Emperor death narrative as a string
    """
    type_text_slowly("\nThe Emperor collapses to his knees.")
    type_text_slowly("Blood spills across the marble floor of the throne room.")
    type_text_slowly("\"So... this is the end,\" he whispers.")
    type_text_slowly("Your blade flashes once more.")
    type_text_slowly("The Emperor of the Rising Sun is slain.\n")

def final_boss_outro_ronin():
    """
    Display the concluding narration after the Ronin successfully defeats the Emperor.

    :precondition: character has chosen the Ronin path
    :precondition: the Emperor has been defeated by the Ronin
    :postcondition: the fall of the Empire narration is printed to the terminal
    :return: the displayed Ronin victory outro as a string
    """
    type_text_slowly("\nThe Emperor's body lies motionless at your feet.")
    type_text_slowly("The throne stands empty.")
    type_text_slowly("For the first time in generations, the Empire has no master.\n")

    type_text_slowly("You have done what countless rebels could not.")
    type_text_slowly("You have ended the rule of the Rising Sun.\n")

def betrayal_confrontation_intro():
    """
    Display the confrontation introduction when Ryūichi reveals his betrayal.

    :precondition: character is "ronin" path and the Emperor has been defeated
    :precondition: the character’s bond with Ryūichi <= -2 and honor <= -4
    :precondition: the character’s betrayal condition has been set to True
    :postcondition: the betrayal confrontation narration is printed
    :return: the displayed betrayal confrontation text as a string
    """
    type_text_slowly("\nYou feel a presence shift behind you.")
    type_text_slowly("Footsteps whisper across the stone.")
    type_text_slowly("Steel leaves its sheath.\n")

    type_text_slowly("Ryūichi slowly raises his blade behind you.")
    type_text_slowly("\"Your choices damned this land,\" he says, voice trembling.")
    type_text_slowly("\"Every village. Every grave.\"")

    type_text_slowly("You do not turn.")
    type_text_slowly("You already know what comes next.\n")

def betrayal_spared_scene():
    """
    Display the scene where Ryūichi chooses to spare the player after betrayal.

    :precondition: character is "ronin" path and the Emperor has been defeated
    :precondition: the character’s bond with Ryūichi >= 3
    :precondition: the character’s betrayal condition has been set to True
    :postcondition: the mercy scene is printed to the terminal
    :return: the displayed spared scene narration as a string
    """
    type_text_slowly("Your grip loosens.")
    type_text_slowly("Your blade lowers to the stone.")
    type_text_slowly("\"Then strike,\" you whisper. \"If that is the end you seek.\"")

    type_text_slowly("Ryūichi’s blade trembles in the air.")
    type_text_slowly("His teeth grind together.")
    type_text_slowly("At last, he turns away.\n")

    type_text_slowly("\"I cannot kill the brother I once loved,\" he mutters.")
    type_text_slowly("His footsteps fade into the smoke.")


def betrayal_duel_scene():
    """
    Display the final duel scene between the player and Ryūichi after betrayal.

    :precondition: character is "ronin" path and the Emperor has been defeated
    :precondition: the character’s bond with Ryūichi <= 3
    :precondition: the character’s betrayal condition has been set to True
    :postcondition: the betrayal duel narration is printed
    :return: the displayed duel scene narration as a string
    """
    type_text_slowly("Your blades rise at the same time.")
    type_text_slowly("There are no words left to save you now.\n")

    type_text_slowly("Steel clashes one last time between brothers.")
    type_text_slowly("The sound echoes through the ruins like a breaking heart.\n")

def rebuild_scene():
    """
    Display the rebuilding ending where the player and Ryūichi restore the Empire together.

    :precondition: character is "ronin" path and the Emperor has been defeated
    :precondition: the character’s bond with Ryūichi >= 3
    :precondition: the character’s betrayal condition has been set to False
    :postcondition: the rebuilding ending narration is printed
    :return: the displayed rebuilding scene narration as a string
    """
    type_text_slowly("\nThe battlefield falls silent.")
    type_text_slowly("Smoke drifts through shattered halls.")
    type_text_slowly("You stand among the dead — breathing.\n")

    type_text_slowly("Ryūichi steps beside you, bloodied but alive.")
    type_text_slowly("\"The Empire is broken,\" he says.")
    type_text_slowly("\"But perhaps… we can shape what rises from its ashes.\"")

    type_text_slowly("He extends his hand.")
    type_text_slowly("Not as a warrior.")
    type_text_slowly("But as your brother once more.\n")

def abandonment_scene():
    """
    Display the ending where Ryūichi abandons the player after the Emperor’s defeat.

    :precondition: character is "ronin" path and the Emperor has been defeated
    :precondition: the character’s bond with Ryūichi <= 3
    :precondition: the character’s betrayal condition has been set to False
    :postcondition: the abandonment ending narration is printed
    :return: the displayed abandonment scene narration as a string
    """

    type_text_slowly("Ryūichi watches you from a distance.")
    type_text_slowly("\"Power has changed you,\" he says quietly.")
    type_text_slowly("\"I will not walk beside another tyrant.\"")

    type_text_slowly("\nYou stand alone upon the ruins of the throne.")
    type_text_slowly("The Empire is yours — but the victory feels hollow.\n")



