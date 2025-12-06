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
    check_if_goal_attained,
    draw_ascii_map
)
from movement import (
    get_user_choice,
    validate_move,
    move_character
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
        if player_character["path"] == "samurai" or "ronin":
            print_intro_story(player_character)
            explain_game_goal(player_character)
    boss_coordinates = (9, 9)
    achieved_final_goal = False

    draw_ascii_map(player_character, boss_coordinates)
    while is_alive(player_character) and not achieved_final_goal:
        draw_ascii_map(player_character, boss_coordinates)
        direction_choice = get_user_choice()
        if direction_choice == "quit":
            print("\nYou walk away from destiny...\n")
            return

        if validate_move(player_character, direction_choice):
            move_character(player_character, direction_choice)
            draw_ascii_map(player_character, boss_coordinates)
            describe_current_location(game_board, player_character)
            execute_challenge(player_character)
            if player_character["hp"] <= 10 and random.randint(1, 3) == 1:
                ryuichi_flashback(player_character)

            if character_has_leveled(player_character):
                execute_level_up(player_character)

            if check_if_goal_attained(player_character, boss_coordinates):
                if player_character["level"] < 3:
                    print("\nA powerful force blocks your path...")
                    print("You feel unprepared to face what lies ahead.")
                    print("You must reach Level 3 before challenging the Emperor!\n")
                    print("Come back here when you are ready to challenge the Emperor\n")
                    draw_ascii_map(player_character, boss_coordinates)
                else:
                    achieved_final_goal = True
        else:
            print("\nYou cannot go that way.\n")

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
