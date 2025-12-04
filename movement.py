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

    >>> test_character = {"x-coordinate": 2, "y-coordinate": 2}
    >>> validate_move(test_character, 1)
    True

    >>> test_character = {"x-coordinate": 0, "y-coordinate": 0}
    >>> validate_move(test_character, 1)
    False
    """
    new_row_location = character["x-coordinate"]
    new_column_location = character["y-coordinate"]

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

    >>> test_character = {"x-coordinate": 2, "y-coordinate": 2}
    >>> move_character(test_character, 1)
    >>> test_character
    {'X-coordinate': 1, 'Y-coordinate': 2}

    >>> test_character = {"x-coordinate": 0, "y-coordinate": 0}
    >>> move_character(test_character, 4)
    >>> test_character
    {'X-coordinate': 0, 'Y-coordinate': -1}
    """

    if direction == 1:
        character["x-coordinate"] -= 1
    elif direction == 2:
        character["x-coordinate"] += 1
    elif direction == 3:
        character["y-coordinate"] += 1
    elif direction == 4:
        character["y-coordinate"] -= 1
    else:
        return