import pyfiglet
import time
import sys
import random

def type_text_slowly(text, delay=0.03):
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
        type_text_slowly("You join arms with Ryūichi to take down the Emperor.\n")

def explain_game_goal(character):
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
    banner = pyfiglet.figlet_format("YOU HAVE DIED", font="doom")
    print(banner)
    type_text_slowly(f"\n{character['name']}'s blade falls into the dust.")
    type_text_slowly("The wind carries your story into silence...\n")

def print_victory_screen(character):
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
    banner = pyfiglet.figlet_format("\nFINAL DUEL", font="slant")
    print(banner)

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


def ryuichi_random_dialogue(character):
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
    if character["path"] == "samurai":
        character["betrayal"] = False
        return
    if character["bond_with_Ryūichi"] < -2 or character["honor"] <= -4:
        character["betrayal"] = True
    else:
        character["betrayal"] = False



def final_boss_intro_samurai():
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
    type_text_slowly("\nRyūichi staggers back, dropping to one knee.")
    type_text_slowly("His blade slips from his fingers and clatters across the stone.\n")

    type_text_slowly("He looks up at you one last time.")
    type_text_slowly("\"Finish it,\" he whispers.")
    type_text_slowly("\"Let the world remember only one of us.\"\n")

def final_boss_intro_ronin():
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
    type_text_slowly("\nThe Emperor collapses to his knees.")
    type_text_slowly("Blood spills across the marble floor of the throne room.")
    type_text_slowly("\"So... this is the end,\" he whispers.")
    type_text_slowly("Your blade flashes once more.")
    type_text_slowly("The Emperor of the Rising Sun is slain.\n")

def final_boss_outro_ronin():
    type_text_slowly("\nThe Emperor's body lies motionless at your feet.")
    type_text_slowly("The throne stands empty.")
    type_text_slowly("For the first time in generations, the Empire has no master.\n")

    type_text_slowly("You have done what countless rebels could not.")
    type_text_slowly("You have ended the rule of the Rising Sun.\n")

def betrayal_confrontation_intro():
    type_text_slowly("\nYou feel a presence shift behind you.")
    type_text_slowly("Footsteps whisper across the stone.")
    type_text_slowly("Steel leaves its sheath.\n")

    type_text_slowly("Ryūichi slowly raises his blade behind you.")
    type_text_slowly("\"Your choices damned this land,\" he says, voice trembling.")
    type_text_slowly("\"Every village. Every grave.\"")

    type_text_slowly("You do not turn.")
    type_text_slowly("You already know what comes next.\n")

def betrayal_spared_scene():
    type_text_slowly("Your grip loosens.")
    type_text_slowly("Your blade lowers to the stone.")
    type_text_slowly("\"Then strike,\" you whisper. \"If that is the end you seek.\"")

    type_text_slowly("Ryūichi’s blade trembles in the air.")
    type_text_slowly("His teeth grind together.")
    type_text_slowly("At last, he turns away.\n")

    type_text_slowly("\"I cannot kill the brother I once loved,\" he mutters.")
    type_text_slowly("His footsteps fade into the smoke.")


def betrayal_duel_scene():
    type_text_slowly("Your blades rise at the same time.")
    type_text_slowly("There are no words left to save you now.\n")

    type_text_slowly("Steel clashes one last time between brothers.")
    type_text_slowly("The sound echoes through the ruins like a breaking heart.")

def rebuild_scene():
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
    type_text_slowly("\nYou stand alone upon the ruins of the throne.")
    type_text_slowly("The Empire is yours — but the victory feels hollow.\n")

    type_text_slowly("Ryūichi watches you from a distance.")
    type_text_slowly("\"Power has changed you,\" he says quietly.")
    type_text_slowly("\"I will not walk beside another tyrant.\"")

    type_text_slowly("Without another word, he turns and disappears into the ruin.")

