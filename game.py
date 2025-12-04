"""
Jameel Mohammed
A01430376
"""
import random

def make_board(rows, columns):
    """
    Create a dictionary-based 5x5 game board filled with random room descriptions.

    :param rows: an integer representing how many rows the board has
    :param columns: an integer representing how many columns the board has
    :precondition: rows and columns must be positive integers greater than zero
    :postcondition: creates a dictionary where each tuple (row, column) has a random room description
    :return: a dictionary representing the game board
    """
    board = {}
    index = 0
    for row in range(rows):
        for column in range(columns):
            room = ["room with 100 gorillas.", "room with 1 ghost.", "room with 1 man fighting 100 gorillas.", "room that reminds you of your youthful days.", "room with another room inside.", "room with a roomba.", "room with a crying BCIT student.", "room with no walls.", "room with no windows.", "room akin to a glass box.", "room with a roommate and a bunk bed.", "room with cleaning drone spraying its windows.", "room with beeping key box by the door.", "room without a functioning heater.", "room with a single laptop displaying an 'A' grade for Lab 8.", "room with 10 pallets of San Pellegrino's Natural Sparkling Water.", "room with 10 pallets of Reese's Peanut Butter Cups (Mega Size).", "room with one small no name brand peanut butter cup.", "room with 50 sniffling students, no tissues and the door is locked.", "room with 1 single tissue and 5 sniffling students (They have to share).", "room with no students because they all graduated successfully.", "room with the crew of the USS Enterprise.", "room full of Wookiees.", "room full of Ewoks.", "room full of Leafs and Habs players."]
            board[(row, column)] = room[index]
            index += 1
    return board

def make_character():
    """
    Create a dictionary that stores the player's starting position and health.

    :precondition: the game must be starting and no character has been created yet
    :postcondition: a new character dictionary is initialized with starting position (0, 0) and full HP (5)
    :return: a dictionary with the keys "X-coordinate", "Y-coordinate", and "Current HP"

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    return character

def describe_current_location(board, character):
    """
    Print the description of the room the player is currently in.

    :param board: a dictionary containing (row, column) tuples as keys and room descriptions as values
    :param character: a dictionary containing the character's current "X-coordinate" and "Y-coordinate"
    :precondition: board must contain valid (row, column) keys and character must have valid coordinates
    :postcondition: prints a message describing the current room and its coordinates
    :return: None

    >>> test_board = {(0, 0): "room with 100 gorillas.", (0, 1): "room with 1 ghost."}
    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
    >>> describe_current_location(test_board, test_character)
    You are currently at (0, 1). It is a room with 1 ghost.
    <BLANKLINE>

    >>> test_board = {(4, 4): "room with 100 gorillas."}
    >>> test_character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5}
    >>> describe_current_location(test_board, test_character)
    You are currently at (4, 4). It is a room with 100 gorillas.
    <BLANKLINE>
    """
    row = character["X-coordinate"]
    column = character["Y-coordinate"]
    if (row, column) in board:
        description = board[(row, column)]
        print(f"You are currently at ({row}, {column}). It is a {description}\n")

def get_user_choice():
    """
    Ask for a direction choice (1–4) and return it as an integer.

    :precondition: user_input must contain a number between 1 and 4
    :postcondition: returns the direction number that the user selected
    :return: an integer representing the chosen direction (1 = North, 2 = South, 3 = East, 4 = West)
    """
    direction_list = [1, 2, 3, 4]
    while True:
        user_input = input("Which direction would you like to go? Please type one of the corresponding numbers:\n1. North\n2. South\n3. East\n4. West\n\nDirection: ")
        if user_input == "":
            print("You must enter a number — don't leave it blank!\n")
            continue
        if not user_input.isdigit():
            print("Please enter a valid number between 1 and 4.\n")
            continue

        direction = int(user_input)
        if direction in direction_list:
            return direction
        else:
            print("Please enter a valid number between 1 and 4.\n")

def validate_move(character, direction):
    """
    Check if the player's move stays within the 5x5 board boundaries.

    :param character: a dictionary containing the character's "X-coordinate" and "Y-coordinate"
    :param direction: an integer (1 = North, 2 = South, 3 = East, 4 = West)
    :precondition: character must have valid coordinates within the 5x5 grid, and direction must be between 1 and 4
    :postcondition: determines whether the move is possible within the grid without changing the character's position
    :return: True if the move is valid, False if it would go off the board

    >>> test_character = {"X-coordinate": 2, "Y-coordinate": 2}
    >>> validate_move(test_character, 1)
    True

    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> validate_move(test_character, 1)
    False
    """
    new_row_location = character["X-coordinate"]
    new_column_location = character["Y-coordinate"]

    if direction == 1:
        new_row_location -= 1
    elif direction == 2:
        new_row_location += 1
    elif direction == 3:
        new_column_location += 1
    elif direction == 4:
        new_column_location -= 1
    else:
        return False

    if new_row_location in range(0, 5) and new_column_location in range(0, 5):
        return True
    else:
        return False

def move_character(character, direction):
    """
    Move the player's position on the 5x5 grid according to the given direction.

    :param character: a dictionary containing the character's "X-coordinate" and "Y-coordinate"
    :param direction: an integer (1 = North, 2 = South, 3 = East, 4 = West)
    :precondition: character must have valid coordinates within the 5x5 grid, and direction must be 1–4
    :postcondition: updates the character's coordinates based on the direction entered
    :return: the updated character dictionary reflecting the new position

    >>> test_character = {"X-coordinate": 2, "Y-coordinate": 2}
    >>> move_character(test_character, 1)
    >>> test_character
    {'X-coordinate': 1, 'Y-coordinate': 2}

    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> move_character(test_character, 4)
    >>> test_character
    {'X-coordinate': 0, 'Y-coordinate': -1}
    """

    if direction == 1:
        character["X-coordinate"] -= 1
    elif direction == 2:
        character["X-coordinate"] += 1
    elif direction == 3:
        character["Y-coordinate"] += 1
    elif direction == 4:
        character["Y-coordinate"] -= 1
    else:
        return

def check_for_foes():
    """
    Randomly determine if the player encounters a foe.

    :postcondition: randomly returns True or False based on a 1 in 4 chance
    :return: True if a foe appears, otherwise False
    """

    if random.randint(1, 4) == 4:
        return True
    else:
        return False

def guessing_game(character):
    """
    A simple number guessing mini-game played when the player enters a trap room.

    :param character: a dictionary containing the player's "X-coordinate", "Y-coordinate", and "Current HP"
    :precondition: character must have valid coordinates and a positive "Current HP" value
    :postcondition: prints messages depending on the guess outcome and may reduce the player's HP
    :return: the updated character dictionary is modified in place to reflect any HP loss
    """

    print(f"You have entered a trap room at ({character["X-coordinate"]}, {character["Y-coordinate"]})! Let's play a game!")
    secret_number = random.randint(0, 5)

    while True:
        guess = input("Guess a number between 0 and 5 inclusive: ")
        if guess == "":
            print("You must enter a number — don't leave it blank!\n")
            continue
        if not guess.isdigit():
            print("Please enter a valid number between 1 and 4.\n")
            continue

        number_guess = int(guess)
        if number_guess == secret_number:
            print("You're right! Keep going!\n")
            break
        elif number_guess < secret_number:
            character["Current HP"] -= 1
            print(f"Too low, the number was {secret_number}. Oh no, you lose 1 HP!\n")
            break
        else:
            character["Current HP"] -= 1
            print(f"Too high, the number was {secret_number}. Oh no, you lose 1 HP!\n")
            break
    print(f"You have {character['Current HP']}HP.")


def is_alive(character):
    """
    Determine whether the player is still alive based on their current HP.

    :param character: a dictionary containing the key "Current HP"
    :precondition: character must contain a numerical "Current HP" value
    :postcondition: evaluates whether the player’s HP is greater than zero
    :return: True if the player’s HP is above 0, otherwise False

    >>> test_character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 5}
    >>> is_alive(test_character)
    True

    >>> test_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 0}
    >>> is_alive(test_character)
    False
    """
    if character["Current HP"] > 0:
        alive = True
    else:
        alive = False
    return alive

def check_if_goal_attained(character):
    """
    Check whether the player has reached the goal position on the 5x5 board.

    :param character: a dictionary containing the character's "X-coordinate" and "Y-coordinate"
    :precondition: character must contain valid integer coordinates between 0 and 4
    :postcondition: evaluates whether the character has reached position (4, 4)
    :return: True if the player has reached the goal, otherwise False

    >>> test_character = {"X-coordinate": 2, "Y-coordinate": 3}
    >>> check_if_goal_attained(test_character)
    False

    >>> test_character = {"X-coordinate": 4, "Y-coordinate": 4}
    >>> check_if_goal_attained(test_character)
    True
    """

    if character["X-coordinate"] == 4 and character["Y-coordinate"] == 4:
        goal = True
    else:
        goal = False
    return goal

def game():
    rows = 5
    columns = 5
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = False
    while is_alive(character) and not achieved_goal:
        describe_current_location(board, character)
        direction = get_user_choice()
        valid_move = validate_move(character, direction)
        if valid_move:
            move_character(character, direction)
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                guessing_game(character)
            achieved_goal = check_if_goal_attained(character)
        else:
            print("Stop right there! You can't go that way.")
    if is_alive(character):
        print("Congratulations! You made it out alive! You have now completed my game!")
    else:
        print("You have died. Your soul will not be taken to Valhalla")


def main():
    print("\nWelcome unsuspecting traveller. You have entered my maze of very fulfilling and exciting rooms! I have left a game in some of my rooms that I wish for you to try! I am quite lonely here so I hope you don't make it out. Best of luck!\n")
    game()


if __name__ == "__main__":
    main()
