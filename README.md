[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1dK8HHJY)
# Blades of the Rising Sun

**COMP 1510 Term Project**

## Developer Information

**Name:** Jameel Mohammed  
**Student Number:** A01430376  
**GitHub Username:** JAMEEEL01

## Project Description

Blades of the Rising Sun is a text-based Single User Dungeon (SUD) adventure game set
in feudal Japan. Players choose between the path of the Samurai or Ronin, navigate a
10x10 grid-based world, face various challenges, and ultimately confront the final boss
at the Emperor's palace. The game features a rich narrative, character progression
through three levels, and multiple endings based on player choices.

## Game Objective

The primary objective of Blades of the Rising Sun is to navigate the 10 x 10 game
board and reach the Emperor's palace at coordinates (9, 9). However, the path you take
and your ultimate goal depend on your chosen path:

- **Ronin Path**: Reach the palace and defeat the Emperor to end his reign. You must
  reach Level 3 before you can enter the palace and face the final boss.
- **Samurai Path**: Reach the palace to protect the Emperor from the rising ronins.
  You must reach Level 3 before you can enter the palace and face your former friend
  Ryūichi, who leads the rebellion.

**Key Objectives:**
1. Navigate the 10 x 10 grid-based world, moving in cardinal directions
2. Encounter and overcome various challenges (combat, riddles, moral dilemmas, etc.)
3. Gain experience points through successful challenge completion
4. Level up from Level 1 to Level 3 (requires 5 XP for Level 2, 10 XP for Level 3)
5. Reach the palace at coordinates (9, 9) while at Level 3
6. Survive the final boss encounter to complete the game

**Game Over Conditions:**
- Your HP reaches 0 (You die)
- You successfully defeat the final boss (Victory!)

## Required Elements

| Required Element | File and Line Number |
|-----------------|---------------------|
| Main function in game.py | `game.py` line 114 |
| Flowchart game.pdf | `Documents/game.pdf` |
| Whimsical, descriptive, and engaging scenario | `user_interface.py` lines 38-56, 81-155 |
| 10x10 grid-based environment | `board.py` line 7 (`make_board` function) |
| Character with name, health/hit points, level, and abilities | `character.py` line 8
  (`make_character` function) |
| Character movement (north/south/east/west) | `movement.py` lines 15-39 (`get_user_choice`), lines
  41-76 (`validate_move`), lines 79-108 (`move_character`) |
| Obstacles when moving | `challenges.py` line 54 (`execute_challenge` function) |
| Opportunities to overcome obstacles | `challenges.py` lines 117-875 (various challenge
  functions) |
| Game ends when character achieves final goal | `game.py` lines 82-93, `board.py` lines 70-88
  (`check_if_goal_attained`) |
| Leveling scheme (levels 1-3) | `character.py` lines 63-85 (`character_has_leveled`), lines
  87-115 (`execute_level_up`) |
| Level names and experience requirements | `character.py` lines 81-84 (Level 1: 5 XP, Level
  2: 10 XP) |
| Health/attributes increase on level up | `character.py` lines 100-101 (max_hp +5,
  attack_power +3) |
| Level 3 can take on boss | `game.py` line 86, `board.py` line 88 (`check_if_goal_attained`) |
| Coherent ecosystem of challenges | `challenges.py` lines 117-875 (24 different challenge types) |
| Game ends if character runs out of HP | `game.py` line 71, `character.py` lines 45-61
  (`is_alive` function) |
| (a) Use of immutable data structures like tuples to minimize unnecessary mutability
  | `board.py` line 49 (tuples as dictionary keys), line 62, line 88 |
| (b) Use of mutable data structures like lists and dictionaries in a thoughtful and
  correct manner | `board.py` line 17 (room_descriptions list), line 45 (board
  dictionary), `character.py` line 28 (character dictionary) |
| (c) Thoughtful use of exceptions and exception handling that prevents the program
  from crashing | Input validation throughout (e.g., `movement.py` lines 30-39,
  `challenges.py` lines 139-140) |
| (d) Minimized scope and lifetime of all variables and objects | Functions use local
  variables and parameters appropriately throughout all modules |
| (e) Decomposition into a collection of small, atomic, independent, and reusable
  functions | All modules demonstrate function decomposition (e.g., `challenges.py` has
  24+ challenge functions, `board.py`, `character.py`, `movement.py` all use modular
  design) |
| (f) Simple flat code that is easy to understand | Code structure is flat and easy
  to understand across all modules |
| (g) Demonstration of understanding of comprehensions through meaningful and correct
  use of one or more list/dictionary comprehensions | `challenges.py` lines 133-136
  (list comprehension filters foes by character level in `combat_challenge`) |
| (h) Selection using if-statements | Throughout all files (e.g., `game.py` lines
  62-65, 86-93, `character.py` lines 81-84, `challenges.py` multiple locations) |
| (i) Repetition using the for-loop and/or the while loop where it makes sense but
  not excessively | `board.py` lines 46-49 (nested for loops), `game.py` line 71 (while
  loop for main game loop), `movement.py` line 23 (while loop for input validation) |
| (j) Use of the membership operator where it makes sense | `movement.py` line 36
  (`direction in [1, 2, 3, 4]`), line 73 (`in range(0, 10)`), `game.py` line 63
  (`skip_tutorial in ["y", "n"]`), `challenges.py` multiple locations (e.g., line
  139: `choice not in ["1", "2", "3"]`) |
| (k) Appropriate use of the range function | `board.py` lines 46-47 (`range(rows)`,
  `range(columns)`), lines 102-104 (`range(10)`), `movement.py` line 73 (`range(0,
  10)`) |
| Thoughtful use of itertools | `challenges.py` line 5 (`from itertools import
  cycle`), line 41 |
| Use of random module | `board.py` line 5, `challenges.py` line 6, used throughout |
| Function annotations | `character.py` line 8 (`make_character(player_name: str,
  path: str) -> dict`) |
| Doctests and/or unit tests for every function | `unit_tests/` directory contains
  comprehensive test coverage |
| All output formatted using f-strings | Throughout all files (e.g., `board.py` line
  49, 63, 66-67, `challenges.py` multiple locations) |

## Project Structure

```
TermProject/
├── Documents/
│   ├── aardwolf_progress.pdf
│   └── game.pdf
├── unit_tests/
│   ├── __init__.py
│   ├── board_unit_tests/
│   │   ├── __init__.py
│   │   ├── test_check_if_goal_attained.py
│   │   ├── test_describe_current_location.py
│   │   └── test_make_board.py
│   ├── challenges_unit_tests/
│   │   ├── __init__.py
│   │   ├── test_ambush_challenge.py
│   │   ├── test_assassin_challenge.py
│   │   ├── test_blessing_challenge.py
│   │   ├── test_bridge_challenge.py
│   │   ├── test_burning_village_challenge.py
│   │   ├── test_duel_of_honor_challenge.py
│   │   ├── test_execution_challenge.py
│   │   ├── test_feast_challenge.py
│   │   ├── test_final_boss_story.py
│   │   ├── test_gamble_challenge.py
│   │   ├── test_healer_challenge.py
│   │   ├── test_hostage_challenge.py
│   │   ├── test_merchant_challenge.py
│   │   ├── test_moral_challenge.py
│   │   ├── test_pilgrim_challenge.py
│   │   ├── test_riddle_challenge.py
│   │   ├── test_sacrifice_challenge.py
│   │   ├── test_shrine_challenge.py
│   │   ├── test_spirit_challenge.py
│   │   ├── test_thief_challenge.py
│   │   ├── test_training_challenge.py
│   │   ├── test_traveler_challenge.py
│   │   └── test_wounded_soldier_challenge.py
│   ├── character_unit_tests/
│   │   ├── __init__.py
│   │   ├── test_character_has_leveled.py
│   │   ├── test_execute_level_up.py
│   │   ├── test_is_alive.py
│   │   └── test_make_character.py
│   └── movement_unit_tests/
│       ├── __init__.py
│       ├── test_get_user_choice.py
│       ├── test_move_character.py
│       └── test_validate_move.py
├── board.py
├── challenges.py
├── character.py
├── game.py
├── movement.py
├── user_interface.py
├── requirements.txt
└── README.md
```

## How to Run

1. Ensure Python 3.x is installed
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the game:
   ```bash
   python game.py
   ```

## Game Features

- **Two Paths**: Choose between Samurai (serve the Emperor) or Ronin (rebel against
  the throne)
- **Dynamic Challenges**: 24 different challenge types including combat, riddles,
  moral dilemmas, and more
- **Character Progression**: Level up from 1 to 3, improving health and attack power
- **Multiple Endings**: Story outcomes vary based on player choices, honor, and bond
  with companion
- **Rich Narrative**: Immersive text-based storytelling with ASCII art and
  slow-typing effects
