import random
from character import (
    make_character,
    is_alive,
    character_has_leveled,
    execute_level_up,
)
from board import (
    make_board,
    describe_current_location,
    draw_ascii_map
)
from movement import (
    get_user_choice,
    validate_move,
    move_character, type_text_slowly
)
from challenges import (
    execute_challenge,
    final_boss_fight,
)
from user_interface import (
    print_title_screen,
    print_intro_story,
    print_death_screen,
    print_victory_screen,
    choose_path,
    determine_betrayal,
    ryuichi_flashback,
    explain_game_goal,
    print_final_duel_banner
)

def game():
    print_title_screen()
    player_name = input("Enter your character's name: ").strip()

    player_path = choose_path()

    game_board = make_board(10, 10)
    player_character = make_character(player_name, player_path)

    while True:
        skip_tutorial = input("Skip tutorial? (Y/N): ").strip().lower()
        if skip_tutorial in ["y", "n"]:
            break
        print("Invalid input. Please enter Y or N.")
    if skip_tutorial != "y":
        print_intro_story(player_character)
        explain_game_goal(player_character)
    boss_coordinates = (9, 9)

    draw_ascii_map(player_character, boss_coordinates)
    while is_alive(player_character):
        direction_choice = get_user_choice()
        if direction_choice == "quit":
            print("\nYou walk away from destiny...\n")
            return
        if not validate_move(player_character, direction_choice):
            print("\nYou cannot go that way.\n")
            continue
        move_character(player_character, direction_choice)

        if (player_character["x-coordinate"] == boss_coordinates[0]
            and player_character["y-coordinate"] == boss_coordinates[1]
        ):
            draw_ascii_map(player_character, boss_coordinates)
            if player_character["level"] < 3:
                type_text_slowly("\nA powerful force blocks your path...")
                type_text_slowly("You feel the Emperor’s presence beyond this point.")
                type_text_slowly("You must reach Level 3 before entering the Emperor's palace!\n")
                type_text_slowly("Come back here when you are ready to approach the Emperor.\n")
                draw_ascii_map(player_character, boss_coordinates)
                continue
            else:
                break
        draw_ascii_map(player_character, boss_coordinates)
        describe_current_location(game_board, player_character)
        execute_challenge(player_character)

        if player_character["hp"] <= 15 and random.randint(1, 3) == 1:
            ryuichi_flashback(player_character)

        if character_has_leveled(player_character):
            execute_level_up(player_character)

    if not is_alive(player_character):
        print_death_screen(player_character)
    else:
        determine_betrayal(player_character)

        if player_character["path"] == "ronin":
            boss_name = "the Emperor"
        else:
            boss_name = player_character["friend_name"]

        print_final_duel_banner(boss_name)

        if final_boss_fight(player_character):
            print_victory_screen(player_character)
        else:
            print_death_screen(player_character)

def main():
    game()

if __name__ == "__main__":
    main()
